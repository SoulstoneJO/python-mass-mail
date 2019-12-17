# python-mass-mail
一个用来群发邮件的python脚本，代码有些粗糙，但是不想改，虽然
心里这么想着，但是后面可能有空还会看看

## 运行环境
Python 版本： Python 3.8

## Excel配置
### 必要字段
    to_name: 接收者的姓名  
    address: 接收者邮件地址，没有检验地址合法性  
    email_subject: 邮件主题(群发时一般都一样，当然你也可以设置成不同的)  
### 可选字段(填充字段):
填充字段都以`#{ ... }`内填充内容构成，一般用于填充html模板eg: `#{name}`,`#{year}`,`#{month}`,`#{date}`;  
填充字段可以继续向后追加，但是请注意，填充字段追加完成后，一定要修改`fields.ini`的相关Excel配置。 
    
## 初始化文件配置
    [mailServer]: 
        smtp服务器设置，请自行谷歌
    [mailContent]:
        mailTemplate: html邮件模板
        from_name: 发送者名称
    [ExcelToList]:
        Excel相关配置 
### 打包后文件目录
    - exe
     - massMail
    - emailTemplate.html
    - fields.ini
配置文件`emTemplate.html`,`fields.ini`,`parameters.xlsx`必须放在可执行文件`massMail.exe`的上一级目录当中，否则会出现闪退，
当然如果你不喜欢这种方式，你也可以通过修改`fields.ini`当中的属性来配置文件位置

## 使用流程
1.配置Excel,设置替代文本字段
2.修改`htmlTemplate.html`
3.修改`fields.ini`配置文件
4.运行`massMail.exe`,群发邮件

## 注意事项
1.程序没有检验邮箱地址是否正确，只有非空检验，填写内容时请注意。
2.Excel配置好后，一定要先保存Excel，否则程序无法读取Excel表格
的内容，并会出现`None`。

