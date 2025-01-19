import re

msg = '謝謝大家的參與，整理了大家的手機號碼如下：0912345678，0923-456678，0934-567-890以及0956 678-901，請多多保持聯絡。'

# 所有的數字
phone_num = ''.join(re.findall(r'\d', msg))

# 轉換格式
formatted_phone_num = [f'{phone_num[i:i+4]}-{phone_num[i+4:i+10]}' for i in range(0, len(phone_num), 10)]

# 輸出
[print(f'第{i+1}個電話號碼： {phone_num}') for i, phone_num in enumerate(formatted_phone_num)]
