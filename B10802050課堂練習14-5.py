import re

msg = '赴酬者聯盟會員輸入聯絡資料，綠巨人好客：0925525252，米國隊長：0935-374-281，擂茶索餌：0942 542-542，X同學：0937-454545，萬吃王0957-575-777，滴嘟人：0975 759475，唉喔面：0965 949 477，黑剮腹：0977777477。'

pattern = r'\d+'\
        r'[-\s]?'\
        r'\d*'\
        r'[-\s]?\d*'

phone_num = re.findall(pattern, msg)
phone_num = [num.replace('-', '').replace(' ', '') for num in phone_num]
[print(f'電話號碼： {num}') for num in phone_num]
