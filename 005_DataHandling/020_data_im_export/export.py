#%% packages
import pandas as pd
import numpy as np

#%%
df = pd.DataFrame({'language': ['R', 'Python', 'SQL', 'R', 'R', 'Python', 'Python'], 
                    'year': [2020, 2020, 2020, 2021, 2022, 2022, 2022],
                    'users': [1E6, 2E6, 0.5E6, 1.1E6, 1.2E6, 2.2E6, 2.4E6]})
df
# %%
df.to_clipboard()
# %%
df.to_excel('languages.xlsx')
# %%
df.to_excel('languages.xlsx', index=False)

#%% excel with multiple sheets
excel_writer = pd.ExcelWriter('languages.xlsx', engine='xlsxwriter')
df.to_excel(excel_writer, sheet_name='basic', index=False)
df.to_excel(excel_writer, sheet_name='advanced', index=False)
# conditional formatting
sheet = excel_writer.sheets['advanced']
cell_range = 'C1:C8'
sheet.conditional_format(cell_range, {'type': '2_color_scale',
                                      'min_value': '1E6',
                                      'max_value': '3E6'})


excel_writer.save()
# %%
df.to_json('languages.json')
# %%
