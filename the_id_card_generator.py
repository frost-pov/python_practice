raw_name=' aLiCe sMiTh '
dept_code='hr-402'
start_year=2024
is_active=True
clean_name=raw_name.strip().title()
dept_id=dept_code.upper()
tenure=2025-start_year
print(isinstance(is_active,bool))
id_card_output=f'ID Card:{clean_name},Dept:{dept_id}Active since:{start_year}Tenure:{tenure}'
print(id_card_output)
status_msg=clean_name+dept_id