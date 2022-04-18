import pandas as pd
import plotly.express as px
df = pd.read_csv("pixel_map_data.csv")
student_df_1 = df.loc[df['student_id']=="TRL_xsl"]
student_df_2 = df.loc[df['student_id']=="TRL_abc"]
student_df_3 = df.loc[df['student_id']=="TRL_xyz"]
student_df_4 = df.loc[df['student_id']=="TRL_zet"]
student_df_5 = df.loc[df['student_id']=="TRL_123"]
student_df_6 = df.loc[df['student_id']=="TRL_imb"]
student_df_7 = df.loc[df['student_id']=="TRL_rst"]
student_df_8 = df.loc[df['student_id']=="TRL_mno"]
student_df_9 = df.loc[df['student_id']=="TRL_987"]
student_df_10 = df.loc[df['student_id']=="TRL_mda"]
student_df_11 = df.loc[df['student_id']=="TRL_zny"]
student_df_1_mean = student_df_1.groupby("level")["attempt"].mean()
student_df_2_mean = student_df_2.groupby("level")["attempt"].mean()
student_df_3_mean = student_df_3.groupby("level")["attempt"].mean()
student_df_4_mean = student_df_4.groupby("level")["attempt"].mean()
student_df_5_mean = student_df_5.groupby("level")["attempt"].mean()
student_df_6_mean = student_df_6.groupby("level")["attempt"].mean()
student_df_7_mean = student_df_7.groupby("level")["attempt"].mean()
student_df_8_mean = student_df_8.groupby("level")["attempt"].mean()
student_df_9_mean = student_df_9.groupby("level")["attempt"].mean()
student_df_10_mean = student_df_10.groupby("level")["attempt"].mean()
student_df_11_mean = student_df_11.groupby("level")["attempt"].mean()

fig = px.scatter()