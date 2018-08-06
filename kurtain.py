from kurtain import kurtain

uf __name__ == '__main__':
    kurtain.debug = True
    port = int(os.environ.get("PORT", 5000))
    kurtain.run (host='0.0.0.0', port=port)
    
