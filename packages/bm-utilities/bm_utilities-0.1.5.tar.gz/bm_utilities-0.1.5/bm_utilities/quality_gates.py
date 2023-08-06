import json
import pandas as pd
import numpy as np
import re



class QualityGates:
#main functions
    value_not_allowed=', value not allowed'
    null_entry=", null entry "
    invalid_format=", invalid format "
    def read_config(self,path):
        with open(path) as json_file:
            data=json.load(json_file)
        return data

    def read_data(self,path):
        data=pd.read_csv(path)
        return data

    def run_Quality_Gates(self,df,config_path):
        config=self.read_config(config_path)
        
        
        if(not self.check_structure(df,config)):
            return
        df["reason_of_rejection"]=""
        df["explanation_of_rejection"]=""

        if("columns_checklist" in config.keys()):
            self.run_columns_checklist(df,config['columns_checklist'])
        if("rows_checklist" in config.keys()):
            self.run_rows_checklist(df,config['rows_checklist'])
        self.clean_rejection_columns(df)
        return df



    def clean_rejection_columns(self,df):
        columns=["reason_of_rejection","explanation_of_rejection"]
        for column_name in columns:
            df[column_name] = df[column_name].apply(lambda x: ','.join(set(filter(None, x.split(',')))).strip(','))


    ###########################################################################################################################################
    #high level checks
    def check_structure(self,df,config):
        ans=True
        
        if("check_number_of_columns" in config):
            if(config["check_number_of_columns"]==True and df.shape[1]!=config["num_columns"]):
                print("number of columns is not matched")
                ans=False
        if ("check_number_of_records" in config):
            num_of_records=config["num_of_records"]
            if (config["check_number_of_records"]==True and df.shape[0]!=num_of_records):
                print("number of records is not matched")
                ans=False
        if("check_number_of_columns" in config):
            if(config["check_number_of_columns"]==True):
                columns_names=config["columns_names"]
                
                df_columns = df.columns.tolist()
                list_set = set(columns_names)
                df_set = set(df_columns)

                missing_in_list = df_set - list_set
                missing_in_df = list_set - df_set

                if missing_in_df or missing_in_list:
                    print("Columns names are not matched")
                    ans=False

        return ans

    def run_rows_checklist(self,df,row_checklist_config):
        print("run_rows_checklist")
        if "completness_check" in row_checklist_config:
            self.completness_check(df,row_checklist_config["completness_check"])
        if "value_validity_check" in row_checklist_config:
            self.value_validity_check(df,row_checklist_config["value_validity_check"])
            
        if "duplicate_entry_check" in row_checklist_config:
            self.duplicate_entry_check(df,row_checklist_config["duplicate_entry_check"])
        if "format_consistency_check" in row_checklist_config:
            self.format_consistency_check(df,row_checklist_config["format_consistency_check"])
        if "cross_field_dependency_check" in row_checklist_config:
            self.cross_field_dependency_check(df,row_checklist_config["cross_field_dependency_check"])
        

    def run_columns_checklist(self,df,column_checklist):
        if "unique_values_check" in column_checklist:
            self.unique_values_check(df,column_checklist["unique_values_check"])
    ###########################################################################################################################################

    #lower level row checks
    def completness_check(self,df,completness_check_config):
        print("completness_check")
        if completness_check_config["check_all"]==True:
            columns_to_check=df.columns.tolist()
        else:
            columns_to_check=completness_check_config["columns_to_check"]
            reason_column = 'reason_of_rejection'
            explanation_column = 'explanation_of_rejection'

            null_rows = df[df[columns_to_check].isnull().any(axis=1)]
            df.loc[null_rows.index, reason_column] += self.null_entry
            df.loc[null_rows.index, explanation_column] = df.loc[null_rows.index, explanation_column] + ", " + df[columns_to_check].apply(
            lambda row: ", ".join("Columns " + col + " are null" for col, is_null in zip(columns_to_check, row.isnull()) if is_null),
            axis=1
        )

    def value_validity_check_numeric(self,df, col_name, column_config):
        print("value_validity_check_numeric")
        values_allowed = column_config["values_allowed"]
        allowed_indices = []
        for allowed_value in values_allowed:
            if "-" in allowed_value:
                start, end = allowed_value.split("-")
                allowed_indices.extend(df.loc[(df[col_name] >= float(start)) & (df[col_name] <= float(end))].index)
            else:
                operator, value = allowed_value[0], allowed_value[1:]
                if operator == ">":
                    allowed_indices.extend(df.loc[df[col_name] > float(value)].index)
                elif operator == ">=":
                    allowed_indices.extend(df.loc[df[col_name] >= float(value)].index)
                elif operator == "<":
                    allowed_indices.extend(df.loc[df[col_name] < float(value)].index)
                elif operator == "<=":
                    allowed_indices.extend(df.loc[df[col_name] <= float(value)].index)
        not_allowed_indices = df.index.difference(allowed_indices)
        df.loc[not_allowed_indices, "reason_of_rejection"] += self.value_not_allowed
        df.loc[not_allowed_indices, "explanation_of_rejection"] += f"Column {col_name} +  value not allowed"

    def value_validity_check_categorical(self,df, col_name, column_config):
        print("value_validity_check_categorical")
        values_allowed = column_config["values_allowed"]
        
        not_allowed_indices = df.loc[~df[col_name].isin(values_allowed)].index
        df.loc[not_allowed_indices, "reason_of_rejection"] += self.value_not_allowed
        df.loc[not_allowed_indices, "explanation_of_rejection"] += ",column " + col_name + " value not allowed"


    def value_validity_check_dates(self,df, col_name, column_config):
        print("value_validity_check_dates")
        values_allowed = column_config["values_allowed"]
        
        allowed_indices = []
        
        for allowed_range in values_allowed:
            if "-" in allowed_range:
                start, end = allowed_range.split("-")
                start_date = pd.to_datetime(start.strip(), dayfirst=True, errors="coerce")
                end_date = pd.to_datetime(end.strip(), dayfirst=True, errors="coerce")
                allowed_indices.extend(df.loc[(df[col_name] >= start_date) & (df[col_name] <= end_date)].index)
            else:
                date_value = pd.to_datetime(allowed_range.strip(), dayfirst=True, errors="coerce")
                allowed_indices.extend(df.loc[df[col_name] == date_value].index)
        
        not_allowed_indices = df.index.difference(allowed_indices)
        df.loc[not_allowed_indices, "reason_of_rejection"] += self.value_not_allowed
        df.loc[not_allowed_indices, "explanation_of_rejection"] += ",column " + col_name + " value not allowed"

    def value_validity_check(self,df,value_validity_check_config):
        print("value_validity_check")
        columns_to_check=list(value_validity_check_config.keys())
        for col in columns_to_check:
            column_config=value_validity_check_config[col]
            if column_config["column_type"]=="numeric":
                self.value_validity_check_numeric(df,col,column_config)
            elif column_config["column_type"]=="categorical":
                self.value_validity_check_categorical(df,col,column_config)
            elif column_config["column_type"]=="dates": 
                self.value_validity_check_dates(df,col,column_config)

        
    def duplicate_entry_check(self,df, duplicate_entry_check_config):
        print("duplicate_entry_check")
        
        if duplicate_entry_check_config["check_all"]:
            columns_to_check = df.columns.tolist()
        else:
            columns_to_check = duplicate_entry_check_config["columns_to_check"]
        
        reason_column = 'reason_of_rejection'
        explanation_column = 'explanation_of_rejection'
        
        duplicate_rows = df[df.duplicated(subset=columns_to_check, keep='first')]
        duplicate_rows_first_occurrence = df.duplicated(subset=columns_to_check, keep='first')
        
        duplicate_indices = duplicate_rows.index.intersection(duplicate_rows_first_occurrence.index)
        
        df.loc[duplicate_indices, reason_column] += ", duplicate"
        
        explanation = "this row is repeated {} times".format(duplicate_rows.groupby(columns_to_check).size().get(0))
        df.loc[duplicate_indices, explanation_column] += explanation
        
        return df


    def format_consistency_check(self,df, format_config):
        print("format_check")
        columns_to_check=list(format_config.keys())
        for col_name in columns_to_check:
            format_regex=format_config[col_name]["format_regex"]
            reason_column = 'reason_of_rejection'
            explanation_column = 'explanation_of_rejection'
            
            invalid_format_rows = df[~df[col_name].astype(str).str.match(format_regex, na=False)]
            
            df.loc[invalid_format_rows.index, reason_column] += self.invalid_format
            df.loc[invalid_format_rows.index, explanation_column] += "Column '{}' has invalid format".format(col_name) +" "
        
        return df

    def cross_field_dependency_check(self,df,cross_field_dependency_check_config):
        for col in list(cross_field_dependency_check_config.keys()):
            dependent_field=col
            dependency_condition=cross_field_dependency_check_config[col]["dependency_condition"]
        # Evaluate the dependency condition for each row in the DataFrame
            dependency_check = df.apply(lambda row: eval(dependency_condition), axis=1)
            
            # Identify the rows where the dependency condition is not satisfied
            invalid_rows = df[~dependency_check]
            
            # Append the reason and explanation for rejection to the respective columns
            reason_column = 'reason_of_rejection'
            explanation_column = 'explanation_of_rejection'
            df.loc[invalid_rows.index, reason_column] += ", invalid dependency"
            df.loc[invalid_rows.index, explanation_column] = df.loc[invalid_rows.index, explanation_column].apply(
                lambda explanation: explanation + ", " if explanation else ""
            ) + "Invalid dependency for " + dependent_field
            
        return df


    #lower level column checks
    def unique_values_check(self,df,column_names):
        ans=True
        for col in column_names:
            if df[col].duplicated().any():
                print(col,"has duplicated values")
                ans=False
        return ans