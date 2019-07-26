# from pyspider.result import ResultWorker
# from pyspider.libs.base_handler import *
# class MyResultWorker(ResultWorker):
#     def on_result(self, task, result):
#         if not result:
#             return
#         #存数据，写接口
#         self.resultdb._replace(tablename='scrapydoc',**self.resultdb._stringify(result))
#
#         super().on_result(task,{'title':result['title']})


from pyspider.result import ResultWorker


class MyResultWorker(ResultWorker):

    def on_result(self, task, result):
        if not result:
            return

        self.resultdb._replace(tablename='aaaa', **self.resultdb._stringify(result))

        # self.resultdb.dbcur.execute('insert into scrapydoc (`title`, `url`, `html`, `content`, `index`) values (%s, %s, %s, %s, %s)', (result['title'], result['url'], result['html'], result['content'], result['index']))

        super().on_result(task, {'title': result['title']})


























