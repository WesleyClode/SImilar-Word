    def predict(self, model, rate, input_word, exist_list, history_1, history_2, history_3):

        if history_1 != '':
            error, exist_list, _ = predict(self, model, rate, history_1, [], '', '', '')
        if history_2 != '':
            error, exist_list, _ = predict(self, model, rate, history_2, exist_list, '', '', '')
        if history_3 != '':
            error, exist_list, _ = predict(self, model, rate, history_3, exist_list, '', '', '')
        #word_list, _=predict(self, rate, input_word, exist_list, '', '')
        error = [0,0,0]
        try:
            #word_list = []
            similar_words = model.most_similar(word, topn=30)
            if word not in exist_list:
                for item in similar_words:
                    if (item[1] > rate) and (item[0] not in exist_list):
                        word_list.append(item[0])
                        exist_list.append(item[0])
            if word in exist_list:
                print("该词以出现，请重新选词！")
                error[0] = 1
                return error, exist_list, []
            else:
                print("给定阈值："+str(rate)+" 下没有满足的词！")
                error[1] = 1
                return error, exist_list, []
        except KeyError:
            print("词汇: "+word+" 不在字典中！")
            error[2] = 1
            return error, exist_list, []
            
        return error, exist_list, result
