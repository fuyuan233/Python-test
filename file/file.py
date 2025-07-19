# Author fuyuan: fuyuan360@qq.com
# Created on 2025/7/19
def sum_last_two_digits(filename):
    total = 0
    line_count = 0

    try:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, 1):
                # 去除行尾换行符并检查空行
                stripped_line = line.strip()
                if not stripped_line:
                    print(f"警告：第{line_number}行为空，已跳过")
                    continue

                # 检查行长度是否足够
                if len(stripped_line) < 2:
                    print(
                        f"错误：第{line_number}行长度不足2个字符（内容：'{stripped_line}'）"
                    )
                    continue

                # 获取后两位字符并尝试转换为数字
                last_two = stripped_line[-2:]
                try:
                    num = float(last_two)  # 支持整数和小数
                    total += num
                    line_count += 1
                except ValueError:
                    print(
                        f"错误：第{line_number}行后两位不是数字（内容：'{last_two}'）"
                    )

    except FileNotFoundError:
        print(f"文件不存在：{filename}")
        return None
    except Exception as e:
        print(f"未知错误：{str(e)}")
        return None

    print(f"成功处理 {line_count} 行数据")
    return total


# 使用示例
filename = "./1.txt"
result = sum_last_two_digits(filename)
if result is not None:
    print(f"所有行后两位数字总和为：{result:.2f}")  # 保留两位小数
