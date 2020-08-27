import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        rate = self.get_argument('rate')
        input_word = self.get_argument('input_word')
        history_1 = self.get_argument('history_1')
        history_2 = self.get_argument('history_2')
        history_3 = self.get_argument('history_3')
        
        from gensim.models import Word2Vec
        model = Word2Vec.load("test_w2v_model_size50_min5_win10")
        exist_list = []
        #error, exist_list, result = self.predict(self, model, rate, input_word, exist_list, history_1, history_2, history_3)
        #self.render('poem.html', rate=rate, input_word=input_word, history_1=history_1,
        #        history_2=history_2, history_3=history_3, result=result)
        
        def get_similar_word(exist_list, word, rate, model = model):
            error = [0,0,0]
            try:
                word_list = []
                similar_words = model.most_similar(word, topn=30)
                print("Input_word: ",word)
                if word not in exist_list:
                    for item in similar_words:
                        print(item)
                        if (item[1] > float(rate)) and (item[0] not in exist_list):
                            word_list.append(item[0])
                            exist_list.append(item[0])
                            print(item[0])
                    if len(word_list) == 0:
                        print("给定阈值："+str(rate)+" 下没有满足的词！")
                        error[1] = 1
                        return error, exist_list, []
                            
                else:
                    if exist_list != []:
                        print("该词已出现，请重新选词！")
                        error[0] = 1
                        return error, exist_list, []
                    
                
            except KeyError:
                print("词汇: "+word+" 不在字典中！")
                error[2] = 1
                return error, exist_list, []
                
            return error, exist_list, word_list
            
        exist_list = []
        error, _, result1 = get_similar_word(exist_list, input_word, rate, model = model)
        print(result1)
        flag = 0
        error_str = ["该词以出现，请重新选词！", "给定阈值："+str(rate)+" 下没有满足的词！", "词汇: "+input_word+" 不在字典中！"]
        for i in range(0,len(error)):
            if error[i] == 1:
                flag = i
        if flag != 0:
            self.render('error.html',rate=rate, input_word = input_word, error = error_str[flag])
        else:
            self.render('poem.html', rate=rate, input_word = input_word, history_1 = history_1, history_2 = history_2, history_3 = history_3, result = result1)
                

        

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/poem', PoemPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
