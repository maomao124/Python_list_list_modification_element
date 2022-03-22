"""
 * Project name(项目名称)：Python_list列表修改元素
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 10:58
 * Version(版本): 1.0
 * Description(描述)： Python_list_list_modification_element
 """

if __name__ == '__main__':
    # 修改单个元素
    num = list(range(0, 21))
    print(num)
    num[6] = -55  # 使用正数索引
    num[-13] = -888  # 使用负数索引
    print(num)

    # 修改一组元素
    num[9:16] = [1, 2, 4]
    print(num)
    # 在4个位置插入元素
    num[4: 4] = [0, 0, 0, 0]
    print(num)
    num[::2] = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]
    print(num)
