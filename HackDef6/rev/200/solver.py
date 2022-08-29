flag = "hackdef{r3vers1ng_g0_1t5_4_fkn_m355_y0u_d1d_1t!}"
key = "J35usD0m"
x = 0
res = ''
for i in flag:
    if x == 8:
        x = 0
    res += hex(ord(i) ^ ord(key[x])) + ','
    x += 1
print(res)