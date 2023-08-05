import pandas as pd

class Cohort():
    @staticmethod
    def count_cohort(df):
        # Generate continuous time series
        time_series = pd.date_range(start=min(df['date']), end=max(df['date']), freq='MS')
        time_series_df = pd.DataFrame({'date': time_series})

        # Get unique user_id values from df
        unique_user_ids = df['user_id'].unique()
        unique_user_ids_df = pd.DataFrame({'user_id': unique_user_ids})

        # Perform cross join with time_series_df
        df_cross_join = pd.merge(unique_user_ids_df, time_series_df, how='cross')

        # Left join df on df_cont
        df_cont = pd.merge(df_cross_join, df, how='left', on=['user_id', 'date'])
        df_cont['count'].fillna(0, inplace=True)

        # Create df_created with user_id and min(date) from df
        df_created = df.groupby('user_id')['date'].min().reset_index()
        df_created.columns = ['user_id', 'created']

        # Left join df_created on df_cont
        df_cont_created = pd.merge(df_cont, df_created, how='left', on='user_id')

        # Calculate cohort column
        df_cont_created['cohort'] = (df_cont_created['date'].dt.to_period('M') - df_cont_created['created'].dt.to_period('M')).apply(lambda r: r.n) * df_cont_created['count']

        df_cont_created['cohort'] = df_cont_created['cohort'].astype(int).astype(str)
        df_cont_created.loc[df_cont_created['cohort'] != "0", 'cohort'] = 't' + df_cont_created['cohort']
        df_cont_created.loc[df_cont_created['date'] == df_cont_created['created'], 'cohort'] = 't' + df_cont_created['cohort']
        df_cont_created.drop(df_cont_created[df_cont_created['cohort'] == '0'].index, inplace=True)

        result = df_cont_created.groupby(['created', 'cohort']).size().reset_index(name='count')

        return result