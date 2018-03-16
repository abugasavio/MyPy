import datetime


class WriteFile:
    def write(self, content):
        file = open(self.filename, 'a+')
        file.write(content + '\n')
        file.close()


class LogFile(WriteFile):
    def __init__(self, filename):
        self.filename = filename

    def write(self, content):
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        content = dt_str + ' ' + content
        super(LogFile, self).write(content)


class DelimFile(WriteFile):
    def __init__(self, filename, delimeter):
        self.filename = filename
        self.delimeter = delimeter

    def write(self, content):
        content = ','.join(content)
        super(DelimFile, self).write(content)
