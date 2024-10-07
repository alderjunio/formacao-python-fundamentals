linguagens = ["python", "js", "c","java", "php"]
linguagens.sort()

linguagens = ["python", "js", "c","java", "php"]
linguagens.sort(reverse=True)

linguagens = ["python", "js", "c","java", "php"]
linguagens.sort(key=lambda x: len(x))

linguagens = ["python", "js", "c","java", "php"]
linguagens.sort(key=lambda x: len(x), reverse=True)