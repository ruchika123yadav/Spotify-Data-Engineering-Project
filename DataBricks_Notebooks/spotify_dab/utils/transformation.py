class reusable:

    def dropColumn(self,df,col):
        df=df.drop(*col)
        return df