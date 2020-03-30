import lib_googletrans as gg

gg.ggtrans_init()

text = 'Hello world'
ret = gg.ggtrans_translate(text, trans_dest='ja')
print(ret)

gg.ggtrans_deinit()
