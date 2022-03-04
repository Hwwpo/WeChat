from jieba import posseg
async def msgget(msg):
    stripped_msg = msg.strip()  # 去掉消息前后的空白字符
    # 使用jieba库进行分词和词性标注
    words = posseg.lcut(stripped_msg)
    city = None
    for word in words:
        if word.flag == 'ns':
            # ns表示地名
            city = word.word
            return city
            break
    return ''