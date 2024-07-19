ori_str = input();

cnt = 0

cnt += ori_str.count("c=")
cnt += ori_str.count("c-")
cnt += ori_str.count("dz=")
ori_str = ori_str.replace("dz=", "1")
cnt += ori_str.count("d-")
cnt += ori_str.count("lj")
cnt += ori_str.count("nj")
cnt += ori_str.count("s=")
cnt += ori_str.count("z=")
ori_str = ori_str.replace("c=", "1")
ori_str = ori_str.replace("c-", "1")

ori_str = ori_str.replace("d-", "1")
ori_str = ori_str.replace("lj", "1")
ori_str = ori_str.replace("nj", "1")
ori_str = ori_str.replace("s=", "1")
ori_str = ori_str.replace("z=", "1")

ori_str = ori_str.replace("1", "")

cnt += len(ori_str)

print(cnt)