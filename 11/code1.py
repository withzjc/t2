#初始编码。 000000001 8位bit= =1个字节   1024byte（字节）= =1kb==1024*8位
#1024kb==1MB   1024MB==1GB  1024GB ==1TB  万国码Unicode：1个字节表示所有额英文和特殊字符数字，
#一个中文要2个字节，16位 65536可能（最开始）；
#32位四个字节， 00000000 00000000 00000000 00000000很浪费啊，
#后面就24位 utf-8，一个中文 3个字节去表示
#gbk是中国的 只包括中文英文。只是国内，一个中文用2个字节


