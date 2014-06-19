import re, codecs

#names = ['germanicus_processed']
#names = [u'appendix', 'calpurnius', 'catullus', 'catullus2', 'germanicus', 'grattius', 'homerus', 'horatius', 'juvenalis', 'lucanus', 'lucretius', 'm_manilius', 'martialis', 'ovidius', 'persius', 'propertius', 'ps_ovid', 'silius', 'statius', 'tibullus', 'val_flaccus', 'vergilius']
text = []
##for name in names:
d = codecs.open('catullus.txt', 'r', 'utf-8')
for d_line in d:
    text += d_line.lower().split() 

vowels = ['a', 'e', 'i', 'u', 'y', 'o']
verb_vowels = ['a', 'e', 'i']
f = codecs.open('dict_without.txt', 'r', 'utf-8')
g = codecs.open('dict.txt', 'r', 'utf-8')
words_in_dict= []
words_with_l = []
comb = {}
notFoundWords = 0
foundWords = 0
percentOfFoundWords = 0

for f_line in f:
    words_in_dict += f_line.lower().split()

for g_line in g:
    words_with_l += g_line.lower().split()

for i in range(len(words_in_dict)):
    for i in range(len(words_with_l)):
        comb[words_in_dict[i]] = words_with_l[i]
   
morf = codecs.open('notation.csv', 'w', 'utf-8') 

for number in range(len(text)):
    text[number] = text[number].strip(',.?<>/;\\":[]{}\|+=_-()*&^%$#@!~')
    word = text[number]
    print word
    
    if len(word)> 2:
        if word[-1] == 'a' and word != 'ill' and word != 'e' and word != 'qu':
            if word in comb:
                morf.write(comb[word] + ' (1.Nom./Abl./Voc.Sg.)' + '\n')

            elif word == 'ossa':
                morf.write('ossă' + ' (3_uniq.Nom./Acc.Pl.)' + '\n')

            elif word.endswith('ta'):
                word = word[:-1]
                word_vb = word[:-1] + 're'
                if word_vb in comb:
                    morf.write(comb[word_vb] + u'tă' + ' (see the auxiliary verb)' + '\n')
                    
            else:
                word_2 = word[:-1] + 'um'
                if word_2 in comb:
                    morf.write(comb[word_2][:-2] + u'ă' + ' (2.Nom./Acc.Pl.)' + '\n')
                #else: в 3-ем склонении ведь еще и гласные меняются, чтобы с этим не мучиться, я сделала так. 
                    #morf.write(comb[word] + ';' + '3.Nom./Acc.Pl.' ) 

        elif word.endswith('ae') and word != 'illae' and word != 'eae' and word != 'quae' and word != 'hae':
            word = word[:-1]
            if word in comb:
                morf.write(comb[word] + 'e' + ' (1.Dat./Gen.Sg./Nom.Pl./Voc.Pl.)' + '\n')


            elif word[-2] == 't': 
                word = word[:-2] 
                word_vb = word + 're'
                if word_vb in comb:
                    morf.write(comb[word_vb][:-2] +  'tae' + ' (see the auxiliary verb)' + '\n')

        elif word.endswith('am'):
            if word[-3] != 'b':
                word = word[:-1]
                verb_con_3 = word[:-2] + 'ere'
                if word in comb and word != 'illa' and word != 'ea' and word != 'qua':
                    morf.write(comb[word] + 'm' + ';' + '1.Acc.Sg.' )
                elif verb_con_3 in comb:
                    morf.write(comb[verb_con_3][:-3] +  u'ăm' + ' (III.Praes.Con.Act.1Sg.)' + '\n') 

            elif word.endswith('eba'):
                word_impf = word[:-2] + 're'
                word_impf_i = word[:-3] + 're'
                if word_impf in comb:
                    morf.write(comb[word_impf][:-3] + u'ēbăm' + ' (II./III.Imperf.Ind.Act.1Sg.)' + '\n')
                elif word_impf_i in comb:
                    morf.write(comb[word_impf_i][:-3] + u'ĭēbăm' + ' (IV.Imperf.Ind.Act.1Sg.)' + '\n')

            elif word.endswith('aba'):
                word_impf = word[:-2] + 're'
                if word_impf in comb:
                    morf.write(comb[word_impf][:-3] + u'ābăm' + ' (I.Imperf.Ind.Act.1Sg.)' + '\n')
                    
            elif word.endswith('ea') and word != 'ea':
                word_prs_con = word[:-1] + 're'
                if word_prs_con in comb:
                    morf.write(comb[word_prs_con][:-2] +  'am' + ' (II.Praes.Con.Act.1Sg.)' + '\n')
            
            elif word.endswith('era'):
                word_fut = word[:-1] + 'ere'
                if word_fut in comb:
                    morf.write(comb[word_fut] +  'm' + ' (Plsqp.Ind.Act.1Sg.)' + '\n')

##            elif word == 'era': вряд ли это работает
##                if text[number-1].endswith('us') or text[number-1].endswith('a') or text[number-1].endswith('um'):
##                    morf.write(comb[word] +  ';' + 'Plsqp. Ind. Act. 1Sg.' )
                
            elif word.endswith('a') and word[-2] != 'r' and word[-2] != 'b' and word[-2] != 'e':
                word_fut = word[:-1] + 'ere'
                word_fut_i = word[:-1] + 're'
                if word_fut in comb:
                    morf.write(comb[word_fut][:-3] +  u'ăm' + ' (III.Praes.Con.Act.1Sg./Fut.I.1Sg.)' + '\n')
                elif word_fut_i in comb:
                    morf.write(comb[word_fut_i][:-2] +  u'ăm' + ' (IV.Praes.Con.Act.1Sg./Fut.I.1Sg.)' + '\n')

            else:
                print 'Some stuff with "am".'

        elif word.endswith('arum'):
            if word[:-3] in comb:
                morf.write(comb[word[:-3]][:-4] + u'ārum' + ' (1.Gen.Pl.)' + '\n')
##            else:
##                print 'Some stuff with "arum".'

        elif word.endswith('is') and word[-3] != 't': # дописать глагольные формы!!
            if word != 'is' and word != 'quis' and word != 'illis' and word != 'eis' and word != 'his'and word != 'nobis' and word != 'vobis':
                stem_1 = word[:-2] + 'a' 
                stem_2 = word[:-2] + 'us'
                stem_3 = word[:-2] + 'um' 
                stem_4 = word[:-3] + 'er' 
                if stem_1 in comb:
                    morf.write(comb[stem_1][:-1] + u'īs' + ' (1.Dat./Abl.Pl.)' + '\n')

                elif word[:-2] in comb:
                    morf.write(comb[word[:-2]] + ' (3cons.Gen.Sg.)' + '\n')

                elif word in comb:
                    morf.write(comb[word] + ' (3mix./3vow.Nom./Gen./Voc.Sg.)' + '\n')

                elif word[:-3] in comb:
                    morf.write(comb[word[:-3]] + ' (3.Gen.Sg.)' + '\n')

                elif stem_2 in comb:
                    morf.write(comb[stem_2][:-2] + u'īs' + ' (2.Dat./Abl.Pl.)' + '\n')

                elif stem_3 in comb:
                    morf.write(comb[stem_3][:-2] + u'īs' + ' (2.Dat./Abl.Pl.)' + '\n')

                elif stem_4 in comb:
                    morf.write(comb[stem_4][:-2] + u'rīs' + ' (2.Dat./Abl.Pl.)' + '\n')

                elif word in comb: #не забыть глагольное -tis! и вообще подумать, как луче прописать 3 скл.
                    morf.write(comb[word] + ' (3.Gen.Sg.)' )

        elif word.endswith('as'):
            word = word[:-1]
            verb_con_3 = word[:-2] + 'ere'
            verb_con_4 = word[:-2] + 're'
            if word in comb and word != 'mensa':
                morf.write(comb[word][:-1] + u'ās' + ' (1.Acc.Pl.)' + '\n')
            elif verb_con_3 in comb:
                morf.write(comb[verb_con_3][:-3] +  u'ās' + ';' + ' (III.Praes.Con.Act.2Sg.)' + '\n')
            elif verb_con_4 in comb:
                morf.write(comb[verb_con_4][-3] + u'ĭās' + ';' + ' (IV.Praes.Con.Act.2Sg.)' + '\n')

            elif word.endswith('a') and len(word) > 3 and word[-3] != 'b' and word[-4] != 'a' and word[-4] != 'e':
                verb_1 = word[:-1] + 're'
                if verb_1 in comb:
                    morf.write(comb[verb_1][:-3] +  u'ās' + ' (I. Praes. Ind. Act. 2Sg.)' + '\n')

            elif word.endswith('ea') and word != 'ea':
                word_prs_con = word[:-1] + 're'
                if word_prs_con in comb:
                    morf.write(comb[word_prs_con][:-2] +  u'ās' + ' (II. Praes. Con. Act. 2Sg.)' + '\n')
   
            elif word.endswith('eba'):
                word_impf = word[:-2] + 're'
                word_impf_i = word[:-3] + 're'
                if word_impf in comb:
                    morf.write(comb[word_impf][:-3] + u'ēbăs' + ' (II./III. Imperf. Ind. Act. 2Sg.)' + '\n')
                elif word_impf_i in comb:
                    morf.write(comb[word_impf_i][:-3] + u'ĭēbăs' + ' (IV. Imperf. Ind. Act. 2Sg.)' + '\n')

            elif word.endswith('ba'):
                word_impf = word[:-2] + 're'
                if word_impf in comb:
                    morf.write(comb[word_impf][:-3] + u'ābăs' + ' (I. Imperf. Ind. Act. 2Sg.)' + '\n')       

        elif word.endswith('ebus'):
            v_word = word[:-3] + 's' 
            if v_word in comb:
                morf.write(v_word[:-4] + u'ēbŭs' + ';' + '5. Dat./Abl. Pl.' )     

        elif word.endswith('us') and word[-4:] != 'ebus' and word[-4:] != 'ubus' and word[-4:] != 'ibus' and word[-4:] != 'urus' and word[-3] != 'm': 
            if word in comb:
                morf.write(comb[word] +  ' (2.Nom.Sg./3cons.Nom./Acc./Voc.Sg./4.Nom./Voc.Sg.)' )
            #elif 
            

        elif word.endswith('er') and word[-3] != 'r':
            if word in comb:
                if word != 'mater' and word != 'pater' and word != 'frater':
                    morf.write(word[:-2] + u'ěr' + ' (2.Dat./Abl.Pl.)' + '\n')
                elif word == 'mater' or word == 'pater' or word == 'frater':
                    morf.write(comb[word] +  ' (3. Nom. Sg.)' ) # а только ли Nom.?

##        elif word.endswith('rer'):
            
            
        elif word.endswith('i'):
            if word != 'mi' and word != 'nemini' and word != 'ei' and word != 'illi' and word != 'hi' and word != 'qui' and word != 'cui' and word != 'mei' and word != 'tui' and word != 'nostri' and word != 'vestri' and word != 'tibi' and word != 'mihi' and word != 'sui' and word != 'sibi': #+куча других местоимений
                ii_word = word[:-1] + 'us'
                ii_word_n = word[:-1] + 'um'
                ii_word_m = word[:-2] + 'er'
                iii_word = word + 's'
                v_word = word[:-1] + 's'
                if word[:-1] in comb:
                    morf.write(comb[word[:-1]] + u'ī' + ' (2.Gen.Sg./Nom.Pl.)' + '\n')
                    
                elif ii_word in comb:
                    morf.write(comb[ii_word][:-2] + u'ī' + ' (2.Gen.Sg./Nom.Pl.)' + '\n')

                elif ii_word_n in comb:
                    morf.write(comb[ii_word_n][:-2] + u'ī' + ' (2.Gen.Sg.)' + '\n')

                elif ii_word_m in comb:
                    morf.write(comb[ii_word_m][:-2] + u'rī' + ' (2.Gen.Sg./Nom.Pl.)' + '\n')

                elif v_word in comb:
                    morf.write(comb[v_word][:-1] + u'ī' + ' (5.Gen./Dat.Sg.)' + '\n')

                elif iii_word in comb: #добавить 3 скл. формы с Gen?
                    morf.write(comb[iii_word][:-1] + u'ī' + ' (3.Dat.Sg./Nom.Pl.)' + '\n')

        elif word.endswith('o'):
            if word != 'illo' and word != 'eo' and word != 'quo' and word != 'nullo':
                ii_word = word[:-1] + 'us'
                ii_word_n = word[:-1] + 'um'
                ii_word_m = word[:-2] + 'er'
                if word[:-1] in comb:
                        morf.write(comb[word[:-1]] + u'ō' + ' (2. Dat./Abl. Sg.)' + '\n')

                elif ii_word in comb:
                        morf.write(comb[ii_word][:-2] + u'ō' + ' (2.Dat./Abl.Sg.)' + '\n')

                elif ii_word_n in comb:
                        morf.write(comb[ii_word_n][:-2] + u'ō' + ' (2.Dat./Abl.Sg.)' + '\n')

                elif ii_word_m in comb:
                        morf.write(comb[ii_word_m][:-2] + u'rō' + ' (2.Dat./Abl.Sg.)' + '\n')

        elif word.endswith('um') and word != 'secum':
            ii_word = word[:-2] + 'us'
            ii_word_m = word[:-3] + 'er'                                 
            if word[-3] != 'r' and word[-2] != 'o':
                if word[:-2] in comb:
                    morf.write(comb[word[:-2]] + u'ŭm' + ' (2.Acc.Sg.)' + '\n')

                elif ii_word in comb:
                    morf.write(comb[ii_word][:-2] + u'ŭm' +  ' (2.Acc.Sg.)' + '\n')

                elif word in comb:
                    morf.write(comb[word][:-2] + u'ŭm' + ' (2.Nom./Acc./Voc.Sg.)' + '\n')

                elif ii_word_m in comb:
                    morf.write(comb[ii_word_m] +  ' (2. Acc. Sg.)' + '\n')

            elif word[-4] == 'r' and word[-3] == 'o':
                ii_word = word[:-4] + 'us'
                ii_word_n = word[:-4] + 'um'
                ii_word_m = word[:-5] + 'er'                   
                if word[:-4] in comb:
                    morf.write(comb[word[:-4]][:-2] + u'ōrŭm' + ' (2.Gen.Pl.)' + '\n')

                elif ii_word in comb:
                    morf.write(comb[ii_word][:-2] + u'ōrŭm' + ' (2.Gen.Pl.)' + '\n')

                elif ii_word_n in comb:
                    morf.write(comb[ii_word_n][:-2] + u'ōrŭm' + ' (2.Gen.Pl.)' + '\n')

                elif ii_word_m in comb:
                    morf.write(comb[ii_word_m][:-2] + u'rōrŭm' + ' (2.Gen.Pl.)' + '\n')
        elif word == 'secum':
            morf.write(u'sĕcŭm' + ';' + 'Adv.')

        elif word.endswith('e') and word[-2] != 'a' and word != 'ille' and word != 'me'  and word != 'te'  and word != 'se': 
            ii_word = word[:-1] +'us' #добавить третье согласное!
            iii_word_com = word[:-1] + 'is'
            v_word = word + 's' 
            if ii_word in comb:
                morf.write(comb[ii_word][:-2] + u'ĕ' + ' (2m.Voc.Sg.)' + '\n')

            elif word in comb:
                morf.write(comb[word][:-1] + u'ĕ' + ' (3vow.Nom./Acc./Voc.Sg.)' + '\n')

            elif iii_word_com in comb:
                morf.write(comb[iii_word_com][:-2] + u'ĕ' + ' (3com.Abl.Sg.)' + '\n')

            elif v_word in comb:
                morf.write(comb[v_word][:-2] + u'ē' + ' (5.Acc.Sg.)' + '\n')

        elif word.endswith('i'):
            ii_word_i = word +'us'
            morf.write(comb[ii_word_i][:-3] + u'ī' + ' (2m.Voc./Gen.Sg.)' + '\n')

        elif word.endswith('orum'):
            stem_2 = word[:-4] + 'us'
            stem_3 = word[:-4] + 'um' 
            stem_4 = word[:-5] + 'er'
            if stem_2 in comb:
                morf.write(comb[stem_2][:-2] + u'ōrum' + ' (2./3cons.Gen.Pl.)' + '\n')

            if stem_3 in comb:
                morf.write(comb[stem_3][:-2] + u'ōrum' + ' (2.Gen.Pl.)' + '\n')

            elif stem_4 in comb:
                morf.write(comb[stem_4][:-2] + u'rōrum' + ' (2.Gen.Pl.)' + '\n')
                
            elif word == 'illorum':
                morf.write(u'illōrum' + ' (that, Gen.Pl.)' + '\n')

            elif word == 'eorum':
                morf.write(u'eōrum' + ' (this, Gen.Pl.)' + '\n') #поправить

            elif word == 'horum':
                morf.write(u'hōrum' + ' (this, Gen.Pl.' + '\n') #поправить

            elif word == 'quorum':
                morf.write(u'quōrum' + ' (this, Gen.Pl.)' + '\n') #поправить

        elif word.endswith('os'):
            stem_2 = word[:-2] + 'us' 
            stem_4 = word[:-3] + 'er'
            if stem_2 in comb:
                morf.write(comb[stem_2][:-2] + u'ōs' + ' (2.Acc.Pl.)' + '\n')

            elif stem_4 in comb:
                morf.write(comb[stem_4][:-2] + u'rōs' + ' (2.Acc.Pl.)' + '\n')

            elif word == 'illos':
                morf.write(u'illōs' + ' (that, m.Acc.Pl.)' + '\n') #поправить

            elif word == 'eos':
                morf.write(u'eōs' + '  (this, m.Acc.Pl.)' + '\n') #поправить

            elif word == 'hos':
                morf.write(u'hōs' + ' (this, m.Acc.Pl.)' + '\n') #поправить

            elif word == 'quos':
                morf.write(u'quōs' + ' (this, m.Acc.Pl.)' + '\n') #поправить

            elif word == 'nos':
                morf.write(u'nōs' + ' (me, Nom./Acc.Pl.)' + '\n')

            elif word == 'vos':
                morf.write(u'vōs' + ' (you, Nom./Acc.Pl.)' + '\n')

        elif word.endswith('es'): #добавить третье согласное!
            iii_word = word[:-2] + 'is'
            if word in comb:
                morf.write(comb[word][:-2] + u'ēs' + ' (5.Nom./Voc.Sg.Nom./Acc./Voc.Pl.)' + '\n')
            elif iii_word in comb:
                morf.write(comb[iii_word][:-2] + u'ēs' + ' (3.Nom./Acc./Voc.Pl.)' + '\n')

        elif word.endswith('ei') and word != 'ei' and word != 'mei':
            v_word = word[:-1] + 's'
            if v_word in comb:
                morf.write(comb[v_word][:-2] + u'eī' + ' (5.Gen./Dat.Sg.)' + '\n')

        elif word.endswith('em'):#добавить третье согласное!
            v_word = word[:-1] + 's'
            iii_word = word[:-2] + 'is'
            if v_word in comb:
                morf.write(comb[v_word][:-2] + u'ĕm' + ' (5.Acc.Sg.)' + '\n')
            elif iii_word in comb:
                morf.write(comb[iii_word][:-2] + u'ĕm' + ' (3.Acc.Sg.)' + '\n')

        elif word == 'rerum' or word == 'dierum': # все легко и просто - добавлять/исправлять нечего.
            morf.write(word[:-4] + u'ērŭm' + ' (5.Gen.Pl.)' + '\n')
            
        elif word == 'rebus' or word == 'diebus': # все легко и просто - добавлять/исправлять нечего.
            morf.write(word[:-4] + u'ēbŭs' + ' (5.Dat./Abl.Sg.)' + '\n')

        elif word.endswith('ui') and word != 'cui' and word != 'qui' and word != 'tui' and word != 'sui':
            iv_word = word[:-1] + 's'
            if iv_word in comb:
                morf.write(comb[iv_word][:-2] + u'ŭī' + ' (4.Dat.Sg.)' + '\n')

            elif word[:-1] in comb:
                morf.write(comb[word[:-1]][:-1] + u'ŭī' + ' (4.Dat.Sg.)' + '\n')

        elif word.endswith('u') and word != 'tu':
            iv_word = word[:-1] + 's'
            if iv_word in comb:
                morf.write(comb[iv_word][:-2] + u'ū' + ' (4.Abl.Sg.)' + '\n')

            elif word[:-1] in comb:
                morf.write(comb[word[:-1]][:-1] + u'ū' + ' (4.Nom./Acc./Voc./Dat./Abl.Sg.)' + '\n')

        elif word.endswith('ua') and word != 'qua':
            if word[:-1] in comb:
                morf.write(comb[word[:-1]][:-1] + u'ŭă' + ' (4.Nom./Voc./Acc.Pl.' + '\n')

        elif word.endswith('uum') and word != 'tu':
            iv_word = word[:-2] + 's'
            if iv_word in comb:
                morf.write(comb[iv_word][:-2] + u'ŭŭm' + ' (4.Gen.Sg.)' + '\n')

            elif word[:-2] in comb:
                morf.write(comb[word[:-2]][:-1] + u'ŭŭm' + ' (4.Gen.Sg.)' + '\n')

        elif word.endswith('ibus'): # добавить 3е скл.!
            iv_word = word[:-4] + 'us'
            iv_word_2 = word[:-4] + 'u'
            if iv_word in comb:
                morf.write(comb[iv_word][:-2] + u'ĭbus' + ' (4.Dat./Abl.Pl.)' + '\n')

            elif iv_word_2 in comb:
                morf.write(comb[iv_word_2][:-1] + u'ĭbus' + ' (4.Dat./Abl.Pl.)' + '\n')

        elif word.endswith('ubus'):
            iv_word = word[:-5] + 'cus'
            number_for_4 = 0
            for letter in range(len(iv_word)):
                if iv_word[letter] in vowels and iv_word[letter] != 'u':
                    number_for_4 += 1
                elif iv_word[letter] == 'u' and iv_word[letter-1] != 'q':
                    number_for_4 += 1
                elif iv_word[letter] == 'u' and iv_word[letter-1] == 'q':
                    continue
                    if number_for_4 == 2 and iv_word in comb:
                        morf.write(comb[iv_word_2][:-1] + u'ubus' + ' (4.Dat./Abl.Pl.)' + '\n')

            if word == 'portubus':
                morf.write('portubus' + ';' + '(4. Dat./Abl. Pl.)' + '\n')

            elif word == 'artubus':
                morf.write(u'artubus' + ';' + '(4. Dat./Abl. Pl.)' + '\n')

            elif word == 'tribubus':
                morf.write(u'tribubus' + ';' + '(4. Dat./Abl. Pl.)' + '\n')

            elif word == 'partubus':
                morf.write(u'partubus' + ';' + '(4. Dat./Abl. Pl.)' + '\n')

            elif word == 'verubus':
                morf.write(u'verubus' + ';' + '(4. Dat./Abl. Pl.)' + '\n')

            elif word == 'quercubus':
                morf.write(u'quercubus' + ';' + '(4. Dat./Abl. Pl.)' + '\n')

        elif word.startswith('ill'): # перевод на англ.!
            if word[3] == 'e' and len(word) == 4:
                morf.write(word[:-3] + 'e' + ';' + 'm. Nom. Sg.' )
            elif word[3] == 'i' and word[4] == 'u' and word[5] == 's' and len(word) == 5:
                morf.write(word[:-3] + 'īus' + ';' + '(m./f./n. Gen. Sg.)' + '\n')
            elif word[3] == 'i' and len(word) == 4:
                morf.write(word[:-3] + 'ī' + ';' + '(m./f./n. Dat. Sg./ m. Nom. Pl.)' + '\n')
            elif word[3] == 'u' and word[4] == 'm' and len(word) == 5:
                morf.write(word[:-3] + 'um' + ';' + '(m. Acc. Sg.)' + '\n')
            elif word[3] == 'o' and len(word) == 4:
                morf.write(word[:-3] + 'ō' + ';' + '(m./n. Abl. Sg.)' + '\n')
            elif word[3] == 'o' and word[4] == 'r' and word[5] == 'u' and word[6] == 'm' and len(word) == 7:
                morf.write(word[:-3] + 'ōrum' + ';' + '(m./n. Gen. Pl.)' + '\n')
            elif word[3] == 'i' and word[4] == 's' and len(word) == 5:
                morf.write(word[:-3] + 'īs' + ';' + '(m./f./n. Dat./Abl. Pl.)' + '\n')
            elif word[3] == 'o' and word[4] == 's' and len(word) == 5:
                morf.write(word[:-3] + 'ōs' + ';' + '(m. Acc. Pl.)' + '\n')
            elif word[3] == 'a' and len(word) == 4:
                morf.write(word[:-3] + 'a' + ';' + '(f. Nom./Abl. Sg./ n. Nom./Acc. Pl.)' + '\n')
            elif word[3] == 'a' and word[4] == 'm' and len(word) == 5:
                morf.write(word[:-3] + 'am' + ';' + '(f. Acc. Sg.)' + '\n')
            elif word[3] == 'a' and word[4] == 'e' and len(word) == 5:
                morf.write(word[:-3] + 'ae' + ';' + '(f. Nom. Pl.)' + '\n')
            elif word[3] == 'a' and word[4] == 'r' and word[5] == 'u' and word[6] == 'm' and len(word) == 7:
                morf.write(word[:-3] + 'ārum' + ';' + '(f. Gen. Pl.)' + '\n')
            elif word[3] == 'a' and word[4] == 's' and len(word) == 5:
                morf.write(word[:-3] + 'ās' + ';' + '(f. Acc. Pl.)' + '\n')
            elif word[3] == 'u' and word[4] == 'd' and len(word) == 5:
                morf.write(word[:-3] + 'ud' + ';' + '(n. Nom./Acc. Sg.)' + '\n')

        elif word[0] == 'e':
            if word == 'is':
                morf.write(word + ';' + '(m. Nom. Sg.)' + '\n')
            elif word == 'id':
                morf.write(word + ';' + '(n. Nom./Acc. Sg.)' + '\n')              
            elif word[1] == 'j' and word[2] == 'u' and word[3] == 'u' and word[4] == 's' and len(word) == 5:
                morf.write('ējus' + ';' + '(m./f./n. Gen. Sg.)' + '\n')
            elif word[1] == 'i' and len(word) == 2:
                morf.write('eī' + ';' + '(m./f./n. Dat. Sg./ m. Nom. Pl.)' + '\n')
            elif word[1] == 'u' and word[2] == 'm' and len(word) == 3:
                morf.write('eum' + ';' + '(m. Acc. Sg.)' + '\n')
            elif word[1] == 'o' and len(word) == 2:
                morf.write('eō' + ';' + '(m./n. Abl. Sg.)' + '\n')
            elif word[1] == 'o' and word[2] == 'r' and word[3] == 'u' and word[4] == 'm' and len(word) == 5:
                morf.write('eōrum' + ';' + '(m./n. Gen. Pl.)' + '\n')
            elif word[1] == 'i' and word[2] == 's' and len(word) == 3:
                morf.write('eīs' + ';' + '(m./f./n. Dat./Abl. Pl.)' + '\n')
            elif word[1] == 'o' and word[2] == 's' and len(word) == 3:
                morf.write('eōs' + ';' + '(m. Acc. Pl.)' + '\n')
            elif word[1] == 'a' and len(word) == 2:
                morf.write('ea' + ';' + '(f. Nom./Abl. Sg./ n. Nom./Acc. Pl.)' + '\n')
            elif word[1] == 'a' and word[2] == 'm' and len(word) == 3:
                morf.write('eam' + ';' + '(f. Acc. Sg.)' + '\n')
            elif word[1] == 'a' and word[2] == 'e' and len(word) == 3:
                morf.write('eae' + ';' + '(f. Nom. Pl.)' + '\n')
            elif word[1] == 'a' and word[2] == 'r' and word[3] == 'u' and word[4] == 'm' and len(word) == 5:
                morf.write('eārum' + ';' + '(f. Gen. Pl.)' + '\n')
            elif word[1] == 'a' and word[2] == 's' and len(word) == 3:
                morf.write('eās' + ';' + '(f. Acc. Pl.)' )

        elif word[:2] == 'qu':
            if len(word) == 3 and word[2] == 'i':
                morf.write(u'quī' + ';' + 'm. Nom. Sg./Pl.' )
            elif len(word) == 4 and word[2] == 'e'and word[3] == 'm':
                morf.write(u'quĕm' + ';' + 'm. Acc. Sg.' )
            elif len(word) == 3 and word[2] == 'o':
                morf.write(u'quō' + ';' + 'm./n. Abl. Sg.' )
            elif len(word) == 4 and word[2] == 'a' and word[3] == 'e':
                morf.write(u'quae' + ';' + 'f. Nom. Sg./Pl./ n. Nom./Acc. Pl.' )
            elif len(word) == 4 and word[2] == 'a' and word[3] == 'm':
                morf.write(u'quăm' + ';' + '(f. Acc. Pl.)' + '\n')
            elif len(word) == 3 and word[2] == 'a':
                morf.write(u'quā' + ';' + '(f. Abl. Pl.)' + '\n')
            elif len(word) == 4 and word[2] == 'o' and word[3] == 'd':
                morf.write(u'quŏd' + ';' + '(n. Nom/Acc. Sg.)' + '\n')
            elif len(word) == 6 and word[2] == 'o' and word[3] == 'r' and word[4] == 'u' and word[5] == 'm':
                morf.write(u'quŏrŭm' + ';' + '(m./n. Gen. Pl.)' + '\n')
            elif len(word) == 6 and word[2] == 'i' and word[3] == 'b' and word[4] == 'u' and word[5] == 's':
                morf.write(u'quĭbŭs' + ';' + '(m./f./n. Dat./Abl. Pl.)' + '\n')
            elif len(word) == 4 and word[2] == 'o' and word[3] == 's':
                morf.write(u'quōs' + ';' + '(m. Acc. Pl.)' + '\n')
            elif len(word) == 6 and word[2] == 'a' and word[3] == 'r' and word[4] == 'u' and word[5] == 'm':
                morf.write(u'quārŭm' + ';' + '(f. Gen. Pl.)'  + '\n')
            elif len(word) == 4 and word[2] == 'a' and word[3] == 's':
                morf.write(u'quās' + ';' + '(f. Acc. Pl.)' + '\n')              
                
        elif word[:2] == 'cu':
            if len(word) == 5 and word[2] == 'j' and word[3] == 'u' and word[4] == 's':
                morf.write(u'cŭjŭs' + ';' + 'm./f./n. Gen. Sg.' + '\n')
            elif len(word) == 3 and word[2] == 'i':
                morf.write(u'cŭī' + ';' + 'm./f./n. Dat. Sg.' + '\n')
            
        elif word == 'ego':
            morf.write(u'ego' + ';' + '"me" Nom. Sg.' + '\n')
        elif word == 'mei':
            morf.write(u'meī' + ';' + '"me" Gen. Sg.' + '\n')
        elif word == 'mihi':
            morf.write(u'mihī' + ';' + '"me" Dat. Sg.' + '\n')
        elif word == 'mi':
            morf.write(u'mi' + ';' + '"me" Dat. Sg.' + '\n')
        elif word == 'tibi':
            morf.write(u'tihī' + ';' + '"you" Dat. Sg.' + '\n')
                           
        elif len(word) == 2 and word[1] == 'e': #включить в общую парадигму на 'e'
            if word[0] == 'm':
                morf.write(u'mē' + ';' + '"me" Acc./Abl. Sg.' + '\n')
            elif word[0] == 't':
                morf.write(u'tē' + ';' + '"you" Acc./Abl. Sg.' + '\n')
            elif word[0] == 's':
                morf.write(u'sē' + ';' + '"yourself" Acc./Abl. Sg./Pl.' + '\n')

        elif len(word) == 3 and word.endswith('os'): #включить в общую парадигму на 'os'
            if word[0] == 'n':
                morf.write(u'nōs' + ';' + '"me" Nom./Acc. Pl.' + '\n')
            elif word[0] == 'v':
                morf.write(u'vōs' + ';' + '"you" Nom./Acc. Pl.' + '\n')

        elif len(word) == 6 and word.endswith('stri'): #включить в общую парадигму на 'os'
            if word.startswith('no'):
                morf.write(u'nostrī' + ';' + '"me" Gen. Pl.' + '\n')
            elif word.startswith('ve'):
                morf.write(u'vestrī' + ';' + '"you" Gen. Pl.' + '\n')

        elif len(word) == 5 and word.endswith('obis'): #включить в общую парадигму на 'os'
            if word.startswith('n'):
                morf.write(u'nōbīs' + ';' + '"me" Dat./Abl. Pl.' + '\n')
            elif word.startswith('v'):
                morf.write(u'vōbīs' + ';' + '"you" Dat./Abl. Pl.' + '\n')

        elif word.endswith('bo'):
            verb_1 = word[:-2] + 're'
            if verb_1 in comb:
                if verb_1[-3] == 'a':
                    morf.write(comb[verb_1][-3] + 'ābō' + '(I. Fut.I Act. 1Sg.)' + '\n')
                elif verb_1[-3] == 'e':
                    morf.write(comb[verb_1][-3] + 'ēbō' + '(II. Fut.I Act. 1Sg.)' + '\n')

        elif word.endswith('o') and word[-2] != 'b' and word[-3] != 'a' and word[-3] != 'e':
            verb_1 = word[:-1] + 'are'
            verb_2_4 = word[:-1] + 're'
            verb_3 = word[:-1] + 'ere'
            if verb_1 in comb:
                morf.write(comb[verb_1][:-3] +  'ō' + ';' + 'I. Praes. Ind. Act. 1Sg.' + '\n')
            elif verb_2_4 in comb:
                if comb[verb_2_4][-3] == 'e':
                    morf.write(comb[verb_2_4][:-3] +  'ō' + ';' + 'II.Praes. Ind. Act. 1Sg.' + '\n')
                elif comb[verb_2_4][-3] == 'i':
                    morf.write(comb[verb_2_4][:-3] +  'ō' + ';' + 'IV.Praes. Ind. Act. 1Sg.' + '\n')
            elif verb_3 in comb:
                morf.write(comb[verb_3][:-3] +  'ō' + ';' + 'III. Praes. Ind. Act. 1Sg.' + '\n')

        elif word.endswith('res'):
            verb_1_imp = word[:-4] + 'are'
            verb_2_3_imp = word[:-4] + 'ere'
            verb_4_imp = word[:-4] + 'ire'
            if verb_1_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + 'ārēs' +'(I. Imperf. Con. Act. 2Sg.)' + '\n')
            elif verb_2_3_imp in comb:
                morf.write(comb[verb_2_3_imp][:-3] + 'erēs' +'(II./III. Imperf. Con. Act. 2Sg.)' + '\n')
            elif verb_4_imp in comb:
                morf.write(comb[verb_4_imp][:-3] + 'īrēs' +'(IV. Imperf. Con. Act. 2Sg.)' + '\n')
                
        elif word.endswith('es') and word[-3] != 'r' and word[-4] not in verb_vowels:
            verb_2 = word[:-1] + 're'
            verb_4_fut = word[:-2] + 're'
            verb_1 = word[:-2] + 'are'
            if verb_4_fut in comb:
                morf.write(comb[verb_4_fut][:-3] + 'ĭĕt' + ';' + 'IV. Fut.I Act. 3Sg.' + '\n')
            elif verb_2 in comb:
                morf.write(comb[verb_2][:-3] +  'ĕt' + ';' + 'II. Praes. Ind. Act. 3Sg./III. Fut.I Act. 3Sg.' + '\n')
            elif verb_1 in comb:
                morf.write(comb[verb_1][:-3] +  'ĕt' + ';' + 'I. Praes. Con. Act. 3Sg.' + '\n')

        elif word.endswith('bis'):
            verb_1 = word[:-2] + 're'
            if verb_1 in comb:
                if verb_1[-3] == 'a':
                    morf.write(comb[verb_1][-3] + 'ābĭs' + '(I. Fut.I Act. 2Sg.)' + '\n')
                elif verb_1[-3] == 'e':
                    morf.write(comb[verb_1][-3] + 'ēbĭs' + '(II. Fut.I Act. 2Sg.)' + '\n')

        elif word.endswith('is') and word[-2] != 'b' and word[-3] != 'a' and word[-3] != 'e':
            verb_4 = word[:-1] + 're'
            verb_3 = word[:-2] + 'ere'
            if verb_3 in comb or verb_4 in comb:
                morf.write(comb[verb_4][:-3] +  'īs' + ';' + 'IV. Praes. Ind. Act. 2Sg.' + '\n')
                morf.write(comb[verb_3][:-3] +  'ĭs' + ';' + 'III. Praes. Ind. Act. 2Sg.' + '\n')

        elif word.endswith('ebat'):
            word_impf = word[:-2] + 're'
            word_impf_i = word[:-3] + 're'
            if word_impf in comb:
                morf.write(comb[word_impf][:-3] + 'ēbăt' + ';' + 'II./III. Imperf. Ind. Act. 1Sg.' )
            elif word_impf_i in comb:
                morf.write(comb[word_impf][:-2] + 'ēbăt' + ';' + 'IV. Imperf. Ind. Act. 1Sg.' )

        elif word.endswith('abat'):
            word_impf = word[:-2] + 're'
            if word_impf in comb:
                morf.write(comb[word_impf][:-3] + 'ābăt' + ';' + 'I. Imperf. Ind. Act. 1Sg.' )

        elif word.endswith('eat'):
                word_prs_con = word[:-1] + 're'
                if word_prs_con in comb:
                    morf.write(comb[word_prs_con][:-2] +  u'ăt' + ';' + 'II. Praes. Con. Act. 3Sg.' + '\n') 

        elif word.endswith('at') and len(word) >= 4 and word[-3] != 'b' and word[-3] != 'e' \
        and word[-4] != 'a' and word[-4] != 'e':
            verb_1 = word[:-1] + 're'
            verb_con_3 = word[:-4] + 'ere'
            if verb_1 in comb:
                morf.write(comb[verb_1][:-3] +  u'ăt' + ';' + 'I. Praes. Ind. Act. 3Sg.' + '\n')
            elif verb_con_3 in comb:
                morf.write(comb[verb_con_3][:-3] +  u'ăt' + ';' + '(III. Praes. Con. Act. 3Sg.)' + '\n')

        elif word.endswith('ret'):
            verb_1_imp = word[:-4] + 'are'
            verb_2_3_imp = word[:-4] + 'ere'
            verb_4_imp = word[:-4] + 'ire'
            if verb_1_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + u'ārĕt' +'(I. Imperf. Con. Act. 3Sg.)' + '\n')
            elif verb_2_3_imp in comb:
                morf.write(comb[verb_2_3_imp][:-3] + u'erĕt' +'(II./III. Imperf. Con. Act. 3Sg.)' + '\n')
            elif verb_4_imp in comb:
                morf.write(comb[verb_4_imp][:-3] + u'īrĕt' +'(IV. Imperf. Con. Act. 3Sg.)' + '\n')

        elif word.endswith('et') and len(word) >= 4 and word[-3] != 'r' and word[-4] not in verb_vowels:
            verb_2 = word[:-1] + 're'
            verb_4_fut = word[:-2] + 're'
            verb_1 = word[:-2] + 'are'
            if verb_4_fut in comb:
                morf.write(comb[verb_4_fut][:-3] + u'ĭĕt' + ';' + 'IV. Fut.I Act. 3Sg.' + '\n')
            elif verb_2 in comb:
                morf.write(comb[verb_2][:-3] + u'ĕt' + ';' + 'II. Praes. Ind. Act. 3Sg./III. Fut.I Act. 3Sg.' + '\n')
            elif verb_1 in comb:
                morf.write(comb[verb_1][:-3] + u'ĕt' + ';' + 'I. Praes. Con. Act. 3Sg.' + '\n')
                

        elif word.endswith('bit'):
            verb_1 = word[:-2] + 're'
            if verb_1 in comb:
                if verb_1[-3] == 'a':
                    morf.write(comb[verb_1][-3] + u'ābĭt' + '(I. Fut.I Act. 3Sg.)' + '\n')
                elif verb_1[-3] == 'e':
                    morf.write(comb[verb_1][-3] + u'ēbĭt' + '(II. Fut.I Act. 3Sg.)' + '\n') 

        elif word.endswith('it') and word[-2] != 'b' and word[-3] != 'a' and word[-3] != 'e':
            verb_4 = word[:-1] + 're'
            verb_3 = word[:-2] + 'ere'
            if verb_3 in comb:
                morf.write(comb[verb_3][:-3] +  u'ĭt' + ';' + 'III.Praes. Ind. Act. 3Sg.' + '\n')
            elif verb_4 in comb:
                morf.write(comb[verb_4][:-3] +  u'ĭt' + ';' + 'IV. Praes. Ind. Act. 3Sg.' + '\n')


        elif word.endswith('eamus'):
            verb_2 = word[:-4] + 're'
            if verb_2 in comb:
                morf.write(comb[verb_2][:-2] + u'ĕāmŭs' + '(II. Praes. Con. Act. 1Pl.)' + '\n')

        elif word.endswith('iamus'):
            verb_4 = word[:-4] + 're'
            if verb_4 in comb:
                morf.write(comb[verb_4][:-2] + u'ĭāmŭs' + '(IV. Praes. Con. Act. 1Pl.)' + '\n')
            
        elif word.endswith('amus') and word[-5] != 'e' and word[-5] != 'b' and word[-5] != 'i':
            verb_1 = word[:-3] + 're'
            if verb_1 in comb:
                morf.write(comb[verb_1][:-3] +  u'āmŭs' + ';' + 'III. Praes. Ind. Act. 1Pl.' + '\n')

        elif word.endswith('remus'):
            verb_1_imp = word[:-4] + 'are'
            verb_2_3_imp = word[:-4] + 'ere'
            verb_4_imp = word[:-4] + 'ire'
            if verb_1_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + u'ārēmŭs' +'(I. Imperf. Con. Act. 1Pl.)')
            elif verb_2_3_imp in comb:
                morf.write(comb[verb_2_3_imp][:-3] + u'erēmŭs' +'(II./III. Imperf. Con. Act. 1Pl.)')
            elif verb_4_imp in comb:
                morf.write(comb[verb_4_imp][:-3] + u'īrēmŭs' +'(IV. Imperf. Con. Act. 1Pl.)')

        elif word.endswith('emus') and len(word) >= 6 and word[-5] != 'r' and word[-6] not in verb_vowels:
            verb_4_fut = word[:-4] + 're'
            verb_2 = word[:-3] + 're'
            verb_1 = word[:-4] + 'are'
            if verb_4_fut in comb:
                 morf.write(comb[verb_4_fut][:-3] + u'ĭēmŭs' + ';' + 'IV. Fut.I Act. 1Pl.' )
            elif verb_2 in comb:
                morf.write(comb[verb_2][:-3] + u'ēmŭs' + ';' + 'II. Praes. Ind. Act. 1Pl./III. Fut.I Act. 1Pl./I. Praes. Con. Act. 1Pl.' + '\n')
            elif verb_1 in comb:
                morf.write(comb[verb_1][:-3] + u'ēmŭs' + ';' + '(I. Praes. Con. Act. 1Pl.)' + '\n')

        elif word.endswith('bimus'):
            verb_1 = word[:-2] + 're'
            if verb_1 in comb:
                if verb_1[-3] == 'a':
                    morf.write(comb[verb_1][-3] + u'ābĭmŭs' + '(I. Fut.I Act. 1Pl.)')
                elif verb_1[-3] == 'e':
                    morf.write(comb[verb_1][-3] + u'ēbĭmŭs' + '(II. Fut.I Act. 1Pl.)')

        elif word.endswith('imus'):
            verb_4 = word[:-3] + 're'
            verb_3 = word[:-4] + 'ere'
            if verb_3 in comb:
                morf.write(comb[verb_3][:-3] + u'ĭmŭs' + ';' + 'III.Praes. Ind. Act. 1Pl.' + '\n')
            elif verb_4 in comb:
                morf.write(comb[verb_4][:-3] + u'īmŭs' + ';' + 'IV. Praes. Ind. Act. 1Pl.' + '\n')

        elif word.endswith('eatis'):
            verb_2 = word[:-4] + 're'
            if verb_2 in comb:
                morf.write(comb[verb_2][:-2] + u'ĕātĭs' + '(I. Praes. Con. Act. 2Pl.)' + '\n')

        elif word.endswith('iatis'):
            verb_4 = word[:-4] + 're'
            if verb_4 in comb:
                morf.write(comb[verb_4][:-2] + u'ĭātĭs' + '(IV. Praes. Con. Act. 2Pl.)' + '\n')

        elif word.endswith('atis') and word[-5] != 'i' and word[-5] != 'e' and word[-5] != 'b':
            verb_1 = word[:-3] + 're'
            verb_con_3 = word[:-4] + 'ere'
            if verb_1 in comb:
                morf.write(comb[verb_1][:-3] + u'ātĭs' + ';' + '(I. Praes. Ind. Act. 2Pl.)' + '\n')
            elif verb_con_3 in comb:
                morf.write(comb[verb_con_3][:-3] + u'ātĭs' + ';' + '(III. Praes. Con. Act. 2Pl.)' + '\n')

        elif word.endswith('retis'):
            verb_1_imp = word[:-4] + 'are'
            verb_2_3_imp = word[:-4] + 'ere'
            verb_4_imp = word[:-4] + 'ire'
            if verb_1_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + u'ārēmŭs' +'(I. Imperf. Con. Act. 2Pl.)')
            elif verb_2_3_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + u'erēmŭs' +'(II./III. Imperf. Con. Act. 2Pl.)')
            elif verb_4_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + u'īrēmŭs' +'(IV. Imperf. Con. Act. 2Pl.)')

        elif word.endswith('etis') and word[-5] != 'r' and word[-6] not in verb_vowels:
            verb_4_fut = word[:-4] + 're'
            verb_2 = word[:-3] + 're'
            verb_1 = word[:-4] + 'are'
            if verb_4_fut in comb:
                morf.write(comb[verb_4_fut][:-3] + u'ĭētĭs' + ';' + 'IV. Fut.I Act. 2Pl.' )           
            elif verb_2 in comb:
                morf.write(comb[verb_2][:-3] + u'ētĭs' + '(II. Praes. Ind. Act. 2Pl./III. Fut.I Act. 2Pl.)' + '\n')
            elif verb_1 in comb:
                morf.write(comb[verb_1][:-3] + u'ētĭs' + '(I. Praes. Con. Act. 2Pl.)' + '\n')

        elif word.endswith('bitis'):
            verb_1 = word[:-2] + 're'
            if verb_1 in comb:
                if verb_1[-3] == 'a':
                    morf.write(comb[verb_1][-3] + u'ābĭtĭs' + '(I. Fut.I Act. 2Pl.)')
                elif verb_1[-3] == 'e':
                    morf.write(comb[verb_1][-3] + u'ēbĭtĭs' + '(II. Fut.I Act. 2Pl.)')

        elif word.endswith('itis') and word[-2] != 'b' and word[-3] != 'a' and word[-3] != 'e':
            verb_4 = word[:-3] + 're'
            verb_3 = word[:-4] + 'ere'
            if verb_3 in comb or verb_4 in comb:
                morf.write(comb[verb_4][:-3] + u'ītĭs' + '(IV. Praes. Ind. Act. 2Pl).' + '\n')
                morf.write(comb[verb_3][:-3] + u'ĭtĭs'  + '(III.Praes. Ind. Act. 2Pl.)' + '\n')

        elif word.endswith('eant'):
            verb_2 = word[:-4] + 're'
            if verb_2 in comb:
                morf.write(comb[verb_2][:-2] + u'ĕātĭs' + '(III. Praes. Con. Act. 3Pl.)' + '\n')

        elif word.endswith('iant'):
            verb_4 = word[:-4] + 're'
            if verb_4 in comb:
                morf.write(comb[verb_4][:-2] + u'ĭātĭs' + '(IV. Praes. Con. Act. 3Pl.)' + '\n')

        elif word.endswith('ant') and word[-5] != 'i' and word[-5] != 'e' and word[-5] != 'b':
            verb_1 = word[:-2] + 're'
            verb_con_3 = word[:-3] + 'ere'
            if verb_1 in comb:
                morf.write(comb[verb_1][:-3] +  u'ănt' + '(I. Praes. Ind. Act. 3Pl.)' + '\n')
            elif verb_con_3 in comb:
                morf.write(comb[verb_con_3][:-3] +  u'ănt' + '(III. Praes. Con. Act. 3Pl.)' + '\n')       

        elif word.endswith('rent'):
            verb_1_imp = word[:-4] + 'are'
            verb_2_3_imp = word[:-4] + 'ere'
            verb_4_imp = word[:-4] + 'ire'
            if verb_1_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + u'ārĕnt' + '(I. Imperf. Con. Act. 3Pl.)')
            elif verb_2_3_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + u'erĕnt' + '(II./III. Imperf. Con. Act. 3Pl.)')
            elif verb_4_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + u'īrĕnt' + '(IV. Imperf. Con. Act. 3Pl.)')

        elif word.endswith('ent') and word[-4] != 'r' and word[-5] not in verb_vowels:
            verb_2 = word[:-2] + 're'
            verb_1 = word[:-3] + 'are'
            verb_4_fut = word[:-4] + 're'
            if verb_4_fut in comb:
                morf.write(comb[verb_4_fut][:-3] + u'ĭĕnt' + 'IV. Fut.I Act. 2Pl.' + '\n')
            elif verb_2 in comb:
                morf.write(comb[verb_2][:-3] +  u'ĕnt' + '(II. Praes. Ind. Act. 3Pl./III. Fut.I Act. 2Pl.)' + '\n')
            elif verb_1 in comb:
                morf.write(comb[verb_1][:-3] +  u'ĕnt' + '(I. Praes. Con. Act. 3Pl.)' + '\n')

        elif word.endswith('bunt'):
            verb_1 = word[:-2] + 're'
            if verb_1 in comb:
                if verb_1[-3] == 'a':
                    morf.write(comb[verb_1][-3] + u'ābŭnt' + '(I. Fut.I Act. 3Pl.)' + '\n')
                elif verb_1[-3] == 'e':
                    morf.write(comb[verb_1][-3] + u'ēbŭnt' + '(II. Fut.I Act. 3Pl.)' + '\n')
        
        elif word.endswith('unt') and word[-2] != 'b' and word[-3] != 'a' and word[-3] != 'e':
            verb_3 = word[:-3] + 'ere'
            if verb_3 in comb:
                morf.write(comb[verb_3][:-3] +  u'ŭnt'  + '(III.Praes. Ind. Act. 3Pl.)' + '\n')

        elif word.endswith('iunt'):
            verb_4 = word[:-3] + 're'
            if verb_4 in comb:
                morf.write(comb[verb_4][:-3] +  u'ĭŭnt' + '(IV. Praes. Ind. Act. 3Pl.)' + '\n')

        elif word.endswith('ebamus'):
            word_impf = word[:-2] + 're'
            word_impf_i = word[:-3] + 're'
            if word_impf in comb:
                morf.write(comb[word_impf][:-3] + u'ēbāmŭs' + '(II./III. Imperf. Ind. Act. 1Pl.)' + '\n')
            elif word_impf_i in comb:
                morf.write(comb[word_impf][:-3] + u'ĭēbāmŭs' + '(IV. Imperf. Ind. Act. 1Pl.)' + '\n')

        elif word.endswith('abamus'):
            word_impf = word[:-2] + 're'
            if word_impf in comb:
                morf.write(comb[word_impf][:-3] + u'ābāmŭs' + '(I. Imperf. Ind. Act. 1Pl.)' + '\n')

        elif word.endswith('ebatis'):
            word_impf = word[:-2] + 're'
            word_impf_i = word[:-3] + 're'
            if word_impf in comb:
                morf.write(comb[word_impf][:-3] + u'ēbātĭs' + '(II./III. Imperf. Ind. Act. 2Pl.)' + '\n')
            elif word_impf_i in comb:
                morf.write(comb[word_impf][:-3] + u'ĭēbātĭs' + '(IV. Imperf. Ind. Act. 2Pl.)' + '\n')

        elif word.endswith('abatis'):
            word_impf = word[:-2] + 're'
            if word_impf in comb:
                morf.write(comb[word_impf][:-3] + u'ābātĭs' + '(I. Imperf. Ind. Act. 2Pl.)' + '\n')

        elif word.endswith('ebant'):
            word_impf = word[:-2] + 're'
            word_impf_i = word[:-3] + 're'
            if word_impf in comb:
                morf.write(comb[word_impf][:-3] + u'ēbānt' + '(II./III. Imperf. Ind. Act. 3Pl.)' + '\n')
            elif word_impf_i in comb:
                morf.write(comb[word_impf][:-3] + u'ĭēbānt' + '(IV. Imperf. Ind. Act. 3Pl.)' + '\n')

        elif word.endswith('abant'):
            word_impf = word[:-2] + 're'
            if word_impf in comb:
                morf.write(comb[word_impf][:-3] + u'ābānt' + '(I. Imperf. Ind. Act. 3Pl.)' + '\n')

        elif word.endswith('rem'):
            verb_1_imp = word[:-4] + 'are'
            verb_2_3_imp = word[:-4] + 'ere'
            verb_4_imp = word[:-4] + 'ire'
            if verb_1_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + u'ārĕm' +'(I. Imperf. Con. Act. 1Sg.)' + '\n')
            if verb_2_3_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + u'erĕm' +'(II./III. Imperf. Con. Act. 1Sg.)' + '\n')
            if verb_4_imp in comb:
                morf.write(comb[verb_1_imp][:-3] + u'īrĕm' +'(IV. Imperf. Con. Act. 1Sg.)' + '\n')

        elif word.endswith('em')and word[-3] != 'r' and word[-4] not in verb_vowels:
            verb_1 = word[:-2] + 'are'
            if verb_1 in comb:
                morf.write(comb[verb_1][:-3] + u'ĕm' + '(I. Praes. Con. Act. 1Sg.)' + '\n')
        
        elif word.endswith('or'):
            if word[-3] == 'e':
                verb_pass_3 = word[:-2] + 're'
                if verb_pass_3 in comb:
                    morf.write(comb[verb_pass_3][:-3] + u'ĕŏr' + '(III. Praes. Ind. Pass. 1Sg.)' + '\n')
            elif word[-3] == 'i':
                verb_pass_4 = word[:-2] + 're'
                if verb_pass_4 in comb:
                    morf.write(comb[verb_pass_4][:-3] + u'ĭŏr' + '(IV. Praes. Ind. Pass. 1Sg.)' + '\n')
            else:
                verb_pass_1 = word[:-2] + 'are'
                verb_pass_2 = word[:-2] + 'ere'
                if verb_pass_1 in comb:
                    morf.write(comb[verb_pass_1][:-3] + u'ĭŏr' + '(I. Praes. Ind. Pass. 1Sg.)' + '\n')
                elif verb_pass_2 in comb:
                    morf.write(comb[verb_pass_2][:-3] + u'ĭŏr' + '(II. Praes. Ind. Pass. 1Sg.)' + '\n')

        elif word.endswith('ris'):
            if word[-4] == 'e':
                verb_ind_pass = word[:-3] + 're'
            elif word[-4] == 'i':
                verb_ind_pass_4 = word[:-3] + 're'
            elif word[-4] == 'a':
                verb_ind_pass_1 = word[:-3] + 're'
                if verb_ind_pass in comb:
                    morf.write(comb[verb_ind_pass][:-3] + u'erĭs' + '(II/III. Praes. Ind. Pass. 2Sg.)' + '\n')
                elif verb_ind_pass_4 in comb:
                    morf.write(comb[verb_ind_pass_4][:-3] + u'īrĭs' + '(IV. Praes. Ind. Pass. 2Sg.)' + '\n')
                elif verb_ind_pass_1 in comb:
                    morf.write(comb[verb_ind_pass_1][:-3] + u'ārĭs' + '(I. Praes. Ind. Pass. 2Sg.)' + '\n')

        elif word.endswith('tur'):
            if word[-4] == 'e':
                verb_ind_pass_2 = word[:-3] + 're'
            elif word[-4] == 'i':
                verb_ind_pass_4 = word[:-3] + 're'
                verb_ind_pass_3 = word[:-4] + 'ere'
            elif word[-4] == 'a':
                verb_ind_pass_1 = word[:-3] + 're'
                if verb_ind_pass_2 in comb:
                    morf.write(comb[verb_ind_pass_2][:-3] + u'ētŭr' + '(II. Praes. Ind. Pass. 3Sg.)' + '\n')
                elif verb_ind_pass_4 in comb:
                    morf.write(comb[verb_ind_pass_4][:-3] + u'ītŭr' + '(IV. Praes. Ind. Pass. 3Sg.)' + '\n')
                elif verb_ind_pass_3 in comb:
                    morf.write(comb[verb_ind_pass_3][:-3] + u'ĭtŭr' + '(III. Praes. Ind. Pass. 3Sg.)' + '\n')
                elif verb_ind_pass_1 in comb:
                    morf.write(comb[verb_ind_pass_1][:-3] + u'ātŭr' + '(I. Praes. Ind. Pass. 3Sg.)' + '\n')

        elif word.endswith('mur'):
            if word[-4] == 'e':
                verb_ind_pass_2 = word[:-3] + 're'
            elif word[-4] == 'i':
                verb_ind_pass_4 = word[:-3] + 're'
                verb_ind_pass_3 = word[:-4] + 'ere'
            elif word[-4] == 'a':
                verb_ind_pass_1 = word[:-3] + 're'
                if verb_ind_pass_2 in comb:
                    morf.write(comb[verb_ind_pass_2][:-3] + u'ēmŭr' + '(II. Praes. Ind. Pass. 1Pl.)' + '\n')
                elif verb_ind_pass_4 in comb:
                    morf.write(comb[verb_ind_pass_4][:-3] + u'īmŭr' + '(IV. Praes. Ind. Pass. 1Pl.)' + '\n')
                elif verb_ind_pass_3 in comb:
                    morf.write(comb[verb_ind_pass_3][:-3] + u'ĭmŭr' + '(III. Praes. Ind. Pass. 1Pl.)' + '\n')
                elif verb_ind_pass_1 in comb:
                    morf.write(comb[verb_ind_pass_1][:-3] + u'āmŭr' + '(I. Praes. Ind. Pass. 1Pl.)' + '\n')

        elif word.endswith('mini'):
            if word[-5] == 'e':
                verb_ind_pass_2 = word[:-4] + 're'
            elif word[-5] == 'i':
                verb_ind_pass_4 = word[:-4] + 're'
                verb_ind_pass_3 = word[:-5] + 'ere'
            elif word[-5] == 'a':
                verb_ind_pass_1 = word[:-4] + 're'
                if verb_ind_pass_2 in comb:
                    morf.write(comb[verb_ind_pass_2][:-3] + u'ēmĭnī' + '(II. Praes. Ind. Pass. 2Pl.)' + '\n')
                elif verb_ind_pass_4 in comb:
                    morf.write(comb[verb_ind_pass_4][:-3] + u'īmĭnī' + '(IV. Praes. Ind. Pass. 2Pl.)' + '\n')
                elif verb_ind_pass_3 in comb:
                    morf.write(comb[verb_ind_pass_3][:-3] + u'ĭmĭnī' + '(III. Praes. Ind. Pass. 2Pl.)' + '\n')
                elif verb_ind_pass_1 in comb:
                    morf.write(comb[verb_ind_pass_1][:-3] + u'āmĭnī' + '(I. Praes. Ind. Pass. 2Pl.)' + '\n')

        elif word.endswith('ntur'):
            if word[-5] == 'e':
                verb_ind_pass_2 = word[:-4] + 're'
            elif word[-5] == 'u':
                verb_ind_pass_4 = word[:-4] + 're'
                verb_ind_pass_3 = word[:-5] + 'ere'
            elif word[-5] == 'a':
                verb_ind_pass_1 = word[:-4] + 're'
                if verb_ind_pass_2 in comb:
                    morf.write(comb[verb_ind_pass_2][:-3] + 'ēntŭr' + '(II. Praes. Ind. Pass. 3Pl.)')
                elif verb_ind_pass_3 in comb:
                    morf.write(comb[verb_ind_pass_3][:-3] + 'ŭntŭr' + '(III. Praes. Ind. Pass. 3Pl.)')
                elif verb_ind_pass_4 in comb:
                    morf.write(comb[verb_ind_pass_4][:-3] + 'ĭŭntŭr' + '(IV. Praes. Ind. Pass. 3Pl.)')
                elif verb_ind_pass_1 in comb:
                    morf.write(comb[verb_ind_pass_1][:-3] + 'ăntŭr' + '(I. Praes. Ind. Pass. 3Pl.)')

        elif word.endswith('bar'):
            if word[-4] == 'a':
                verb_praes_pass_1 = word[:-3] + 're'
                if verb_praes_pass_1 in comb:
                    morf.write(comb[verb_praes_pass_1][:-3] + 'ābăr' + '(I. Praes. Ind. Pass. 1Sg.)')
            elif word[-5] == 'i' and word[-4] == 'e':
                verb_praes_pass_4 = word[:-4] + 're'
                if verb_praes_pass_4 in comb:
                    morf.write(comb[verb_praes_pass_4][:-3] + 'ĭēbăr' + '(IV. Praes. Ind. Pass. 1Sg.)')
            elif word[-4] == 'e':
                verb_praes_pass = word[:-3] + 're'
                if verb_praes_pass in comb:
                    morf.write(comb[verb_praes_pass][:-3] + 'ēbăr' + '(II/III. Praes. Ind. Pass. 1Sg.)')

        elif word.endswith('baris'):
            if word[-6] == 'a':
                verb_praes_pass_1 = word[:-5] + 're'
                if verb_praes_pass_1 in comb:
                    morf.write(comb[verb_praes_pass_1][:-3] + 'ābărĭs' + '(I. Praes. Ind. Pass. 2Sg.)')
            elif word[-7] == 'i' and word[-6] == 'e':
                verb_praes_pass_4 = word[:-6] + 're'
                if verb_praes_pass_4 in comb:
                    morf.write(comb[verb_praes_pass_4][:-3] + 'ĭēbărĭs' + '(IV. Praes. Ind. Pass. 2Sg.)')
            elif word[-6] == 'e':
                verb_praes_pass = word[:-5] + 're'
                if verb_praes_pass in comb:
                    morf.write(comb[verb_praes_pass][:-3] + 'ēbărĭs' + '(II/III. Praes. Ind. Pass. 2Sg.)')

        elif word.endswith('batur'):
            if word[-6] == 'a':
                verb_praes_pass_1 = word[:-5] + 're'
                if verb_praes_pass_1 in comb:
                    morf.write(comb[verb_praes_pass_1][:-3] + 'ābătŭr' + '(I. Praes. Ind. Pass. 3Sg.)')
            elif word[-7] == 'i' and word[-6] == 'e':
                verb_praes_pass_4 = word[:-6] + 're'
                if verb_praes_pass_4 in comb:
                    morf.write(comb[verb_praes_pass_4][:-3] + 'ĭēbătŭr' + '(IV. Praes. Ind. Pass. 3Sg.)')
            elif word[-6] == 'e':
                verb_praes_pass = word[:-5] + 're'
                if verb_praes_pass in comb:
                    morf.write(comb[verb_praes_pass][:-3] + 'ēbătŭr' + '(II/III. Praes. Ind. Pass. 3Sg.)')

        elif word.endswith('bamur'):
            if word[-6] == 'a':
                verb_praes_pass_1 = word[:-5] + 're'
                if verb_praes_pass_1 in comb:
                    morf.write(comb[verb_praes_pass_1][:-3] + 'ābămŭr' + '(I. Praes. Ind. Pass. 1Pl.)')
            elif word[-7] == 'i' and word[-6] == 'e':
                verb_praes_pass_4 = word[:-6] + 're'
                if verb_praes_pass_4 in comb:
                    morf.write(comb[verb_praes_pass_4][:-3] + 'ĭēbămŭr' + '(IV. Praes. Ind. Pass. 1Pl.)')
            elif word[-6] == 'e':
                verb_praes_pass = word[:-5] + 're'
                if verb_praes_pass in comb:
                    morf.write(comb[verb_praes_pass][:-3] + 'ēbămŭr' + '(II/III. Praes. Ind. Pass. 1Pl.)')

        elif word.endswith('bamini'):
            if word[-7] == 'a':
                verb_praes_pass_1 = word[:-6] + 're'
                if verb_praes_pass_1 in comb:
                    morf.write(comb[verb_praes_pass_1][:-3] + 'ābămĭnī' + '(I. Praes. Ind. Pass. 2Pl.)')
            elif word[-8] == 'i' and word[-7] == 'e':
                verb_praes_pass_4 = word[:-7] + 're'
                if verb_praes_pass_4 in comb:
                    morf.write(comb[verb_praes_pass_4][:-3] + 'ĭēbămĭnī' + '(IV. Praes. Ind. Pass. 2Pl.)')
            elif word[-7] == 'e':
                verb_praes_pass = word[:-6] + 're'
                if verb_praes_pass in comb:
                    morf.write(comb[verb_praes_pass][:-3] + 'ēbămĭnī' + '(II/III. Praes. Ind. Pass. 2Pl.)')

        elif word.endswith('bantur'):
            if word[-7] == 'a':
                verb_praes_pass_1 = word[:-6] + 're'
                if verb_praes_pass_1 in comb:
                    morf.write(comb[verb_praes_pass_1][:-3] + 'ābăntŭr' + '(I. Praes. Ind. Pass. 3Pl.)')
            elif word[-8] == 'i' and word[-7] == 'e':
                verb_praes_pass_4 = word[:-7] + 're'
                if verb_praes_pass_4 in comb:
                    morf.write(comb[verb_praes_pass_4][:-3] + 'ĭēbăntŭr' + '(IV. Praes. Ind. Pass. 3Pl.)')
            elif word[-7] == 'e':
                verb_praes_pass = word[:-6] + 're'
                if verb_praes_pass in comb:
                    morf.write(comb[verb_praes_pass][:-3] + 'ebăntŭr' + '(II/III. Praes. Ind. Pass. 3Pl.)')

        elif word.endswith('bor'):
            if word[-4] == 'a':
                verb_fut_pass_1 = word[:-3] + 're'
                if verb_fut_pass_1 in comb:
                    morf.write(comb[verb_fut_pass_1][:-3] + 'ābŏr' + '(I. Fut. I Pass. 1Sg.)')
            elif word[-4] == 'e':
                verb_fut_pass_2 = word[:-3] + 're'
                if verb_fut_pass_2 in comb:
                    morf.write(comb[verb_fut_pass_2][:-3] + 'ēbŏr' + '(II. Fut. I Pass. 1Sg.)')

        elif word.endswith('ar'):
            if word[-3] == 'i':
                verb_fut_pass_4 = word[:-2] + 're'
                if verb_fut_pass_4 in comb:
                    morf.write(comb[verb_fut_pass_4][:-3] + 'ĭăr' + '(IV. Fut. I Pass. 2Sg.)')
            else:
                verb_fut_pass_3 = word[:-2] + 'ere'
                if verb_fut_pass_3 in comb:
                    morf.write(comb[verb_fut_pass_3][:-3] + 'ăr' + '(III. Fut. I Pass. 2Sg.)')

        elif word.endswith('beris'):
            if word[-6] == 'a':
                verb_fut_pass_1 = word[:-5] + 're'
                if verb_fut_pass_1 in comb:
                    morf.write(comb[verb_fut_pass_1][:-3] + 'ābĕrĭs' + '(I. Fut. I Pass. 2Sg.)')
            elif word[-6] == 'e':
                verb_fut_pass_2 = word[:-5] + 're'
                if verb_fut_pass_2 in comb:
                    morf.write(comb[verb_fut_pass_2][:-3] + 'ēbĕrĭs' + '(II. Fut. I Pass. 2Sg.)')

        elif word.endswith('eris'):
            if word[-5] == 'i':
                verb_fut_pass_4 = word[:-4] + 're'
                if verb_fut_pass_4 in comb:
                    morf.write(comb[verb_fut_pass_4][:-3] + 'ĭērĭs' + '(IV. Fut. I Pass. 2Sg.)')
            else:
                verb_fut_pass_3 = word[:-3] + 're'
                if verb_fut_pass_3 in comb:
                    morf.write(comb[verb_fut_pass_3][:-3] + 'ērĭs' + '(III. Fut. I Pass. 2Sg.)')

        elif word.endswith('bitur'):
            if word[-6] == 'a':
                verb_fut_pass_1 = word[:-5] + 're'
                if verb_fut_pass_1 in comb:
                    morf.write(comb[verb_fut_pass_1][:-3] + 'ābĭtŭr' + '(I. Fut. I Pass. 3Sg.)')
            elif word[-6] == 'e':
                verb_fut_pass_2 = word[:-5] + 're'
                if verb_fut_pass_2 in comb:
                    morf.write(comb[verb_fut_pass_2][:-3] + 'ēbĭtŭr' + '(II. Fut. I Pass. 3Sg.)')

        elif word.endswith('etur'):
            if word[-5] == 'i':
                verb_fut_pass_4 = word[:-4] + 're'
                if verb_fut_pass_4 in comb:
                    morf.write(comb[verb_fut_pass_4][:-3] + 'ĭētŭr' + '(IV. Fut. I Pass. 3Sg.)')
            else:
                verb_fut_pass_3 = word[:-3] + 're'
                if verb_fut_pass_3 in comb:
                    morf.write(comb[verb_fut_pass_3][:-3] + 'ētŭr' + '(III. Fut. I Pass. 3Sg.)')                
                
        elif word.endswith('bimur'):
            if word[-6] == 'a':
                verb_fut_pass_1 = word[:-5] + 're'
                if verb_fut_pass_1 in comb:
                    morf.write(comb[verb_fut_pass_1][:-3] + 'ābĭmŭr' + '(I. Fut. I Pass. 1Pl.)')
            elif word[-6] == 'e':
                verb_fut_pass_2 = word[:-5] + 're'
                if verb_fut_pass_2 in comb:
                    morf.write(comb[verb_fut_pass_2][:-3] + 'ēbĭmŭr' + '(II. Fut. I Pass. 1Pl.)')

        elif word.endswith('emur'):
            if word[-5] == 'i':
                verb_fut_pass_4 = word[:-4] + 're'
                if verb_fut_pass_4 in comb:
                    morf.write(comb[verb_fut_pass_4][:-3] + 'ĭēmŭr' + '(IV. Fut. I Pass. 1Pl.)')
            else:
                verb_fut_pass_3 = word[:-3] + 're'
                if verb_fut_pass_3 in comb:
                    morf.write(comb[verb_fut_pass_3][:-3] + 'ēmŭr' + '(III. Fut. I Pass. 1Pl.)')

        elif word.endswith('bimini'):
            if word[-7] == 'a':
                verb_fut_pass_1 = word[:-6] + 're'
                if verb_fut_pass_1 in comb:
                    morf.write(comb[verb_fut_pass_1][:-3] + 'ābĭmĭnī' + '(I. Fut. I Pass. 2Pl.)')
            elif word[-7] == 'e':
                verb_fut_pass_2 = word[:-6] + 're'
                if verb_fut_pass_2 in comb:
                    morf.write(comb[verb_fut_pass_2][:-3] + 'ēbĭmĭnī' + '(II. Fut. I Pass. 2Pl.)')

        elif word.endswith('emini'):
            if word[-6] == 'i':
                verb_fut_pass_4 = word[:-5] + 're'
                if verb_fut_pass_4 in comb:
                    morf.write(comb[verb_fut_pass_4][:-3] + 'ĭēmĭnī' + '(IV. Fut. I Pass. 2Pl.)')
            else:
                verb_fut_pass_3 = word[:-4] + 're'
                if verb_fut_pass_3 in comb:
                    morf.write(comb[verb_fut_pass_3][:-3] + 'ēmĭnī' + '(III. Fut. I Pass. 2Pl.)')

        elif word.endswith('buntur'):
            if word[-7] == 'a':
                verb_fut_pass_3 = word[:-6] + 're'
                if verb_fut_pass_3 in comb:
                    morf.write(comb[verb_fut_pass_1][:-3] + 'ābŭntŭr' + '(I. Fut. I Pass. 1Pl.)')
            elif word[-7] == 'e':
                verb_fut_pass_3 = word[:-6] + 're'
                if verb_fut_pass_3 in comb:
                    morf.write(comb[verb_fut_pass_2][:-3] + 'ēbŭntŭr' + '(II. Fut. I Pass. 1Pl.)')

        elif word.endswith('entur'):
            if word[-5] == 'i':
                verb_fut_pass_3 = word[:-4] + 're'
                if verb_fut_pass_3 in comb:
                    morf.write(comb[verb_fut_pass_4][:-3] + 'ĭēntŭr' + '(IV. Fut. I Pass. 1Pl.)')
            else:
                verb_fut_pass_3 = word[:-4] + 're'
                if verb_fut_pass_3 in comb:
                    morf.write(comb[verb_fut_pass_3][:-3] + 'ēntŭr' + '(III. Fut. I Pass. 1Pl.)')

        elif word.endswith('er'):
            praes_conj_pass_1 = word[:-2] + 'are'
            if praes_conj_pass_1 in comb:
                morf.write(comb[praes_conj_pass_1][:-3] + 'ĕr' + '(I. Praes. Conj. Pass. 1Sg.)')
        elif word.endswith('ear'):
            praes_conj_pass_2 = word[:-2] + 're'
            if praes_conj_pass_2 in comb:
                morf.write(comb[praes_conj_pass_2][:-3] + 'ĕăr' + '(II. Praes. Conj. Pass. 1Sg.)')
        elif word.endswith('iar'):
            praes_conj_pass_4 = word[:-2] + 're'
            if praes_conj_pass_4 in comb:
                morf.write(comb[praes_conj_pass_4][:-3] + 'ĭăr' + '(IV. Praes. Conj. Pass. 1Sg.)')
        elif word.endswith('ar'):
            praes_conj_pass_3 = word[:-2] + 'ere'
            if praes_conj_pass_3 in comb:
                morf.write(comb[praes_conj_pass_3][:-3] + 'ăr' + '(III. Praes. Conj. Pass. 1Sg.)')

        elif word.endswith('eris'):
            praes_conj_pass_1 = word[:-4] + 'are'
            if praes_conj_pass_1 in comb:
                morf.write(comb[praes_conj_pass_1][:-3] + 'ērĭs' + '(I. Praes. Conj. Pass. 2Sg.)')
        elif word.endswith('earis'):
            praes_conj_pass_2 = word[:-4] + 're'
            if praes_conj_pass_2 in comb:
                morf.write(comb[praes_conj_pass_2][:-3] + 'ĕārĭs' + '(II. Praes. Conj. Pass. 2Sg.)')
        elif word.endswith('iaris'):
            praes_conj_pass_4 = word[:-4] + 're'
            if praes_conj_pass_4 in comb:
                morf.write(comb[praes_conj_pass_4][:-3] + 'ĭārĭs' + '(IV. Praes. Conj. Pass. 2Sg.)')
        elif word.endswith('aris'):
            praes_conj_pass_3 = word[:-4] + 'ere'
            if praes_conj_pass_3 in comb:
                morf.write(comb[praes_conj_pass_3][:-3] + 'ārĭs' + '(III. Praes. Conj. Pass. 2Sg.)')

        elif word.endswith('etur'):
            praes_conj_pass_1 = word[:-4] + 'are'
            if praes_conj_pass_1 in comb:
                morf.write(comb[praes_conj_pass_1][:-3] + 'ētŭr' + '(I. Praes. Conj. Pass. 3Sg.)')
        elif word.endswith('eatur'):
            praes_conj_pass_2 = word[:-4] + 're'
            if praes_conj_pass_2 in comb:
                morf.write(comb[praes_conj_pass_2][:-3] + 'ĕātŭr' + '(II. Praes. Conj. Pass. 3Sg.)')
        elif word.endswith('iatur'):
            praes_conj_pass_4 = word[:-4] + 're'
            if praes_conj_pass_4 in comb:
                morf.write(comb[praes_conj_pass_4][:-3] + 'ĭātŭr' + '(IV. Praes. Conj. Pass. 3Sg.)')
        elif word.endswith('atur'):
            praes_conj_pass_3 = word[:-4] + 'ere'
            if praes_conj_pass_3 in comb:
                morf.write(comb[praes_conj_pass_3][:-3] + 'ātŭr' + '(III. Praes. Conj. Pass. 3Sg.)')

        elif word.endswith('emur'):
            praes_conj_pass_1 = word[:-4] + 'are'
            if praes_conj_pass_1 in comb:
                morf.write(comb[praes_conj_pass_1][:-3] + 'ēmŭr' + '(I. Praes. Conj. Pass. 1Pl.)')
        elif word.endswith('eamur'):
            praes_conj_pass_2 = word[:-4] + 're'
            if praes_conj_pass_2 in comb:
                morf.write(comb[praes_conj_pass_2][:-3] + 'ĕāmŭr' + '(II. Praes. Conj. Pass. 1Pl.)')
        elif word.endswith('iamur'):
            praes_conj_pass_4 = word[:-4] + 're'
            if praes_conj_pass_4 in comb:
                morf.write(comb[praes_conj_pass_4][:-3] + 'ĭāmŭr' + '(IV. Praes. Conj. Pass. 1Pl.)')
        elif word.endswith('amur'):
            praes_conj_pass_3 = word[:-4] + 'ere'
            if praes_conj_pass_3 in comb:
                morf.write(comb[praes_conj_pass_3][:-3] + 'āmŭr' + '(III. Praes. Conj. Pass. 1Pl.)')

        elif word.endswith('emini'):
            praes_conj_pass_1 = word[:-5] + 'are'
            if praes_conj_pass_1 in comb:
                morf.write(comb[praes_conj_pass_1][:-3] + 'ēmĭnī' + '(I. Praes. Conj. Pass. 2Pl.)')
        elif word.endswith('eamini'):
            praes_conj_pass_2 = word[:-5] + 're'
            if praes_conj_pass_2 in comb:
                morf.write(comb[praes_conj_pass_2][:-3] + 'ĕāmĭnī' + '(II. Praes. Conj. Pass. 2Pl.)')
        elif word.endswith('iamini'):
            praes_conj_pass_4 = word[:-5] + 're'
            if praes_conj_pass_4 in comb:
                morf.write(comb[praes_conj_pass_4][:-3] + 'ĭāmĭnī' + '(IV. Praes. Conj. Pass. 2Pl.)')
        elif word.endswith('amini'):
            praes_conj_pass_3 = word[:-5] + 'ere'
            if praes_conj_pass_3 in comb:
                morf.write(comb[praes_conj_pass_3][:-3] + 'āmĭnī' + '(III. Praes. Conj. Pass. 2Pl.)')

        elif word.endswith('entur'):
            praes_conj_pass_1 = word[:-5] + 'are'
            if praes_conj_pass_1 in comb:
                morf.write(comb[praes_conj_pass_1][:-3] + 'ēntŭr' + '(I. Praes. Conj. Pass. 3Pl.)')
        elif word.endswith('eantur'):
            praes_conj_pass_2 = word[:-5] + 're'
            if praes_conj_pass_3 in comb:
                morf.write(comb[praes_conj_pass_3][:-3] + 'ĕāntŭr' + '(II. Praes. Conj. Pass. 3Pl.)')
        elif word.endswith('iantur'):
            praes_conj_pass_4 = word[:-5] + 're'
            if praes_conj_pass_4 in comb:
                morf.write(comb[praes_conj_pass_4][:-3] + 'ĭāntŭr' + '(IV. Praes. Conj. Pass. 3Pl.)')
        elif word.endswith('antur'):
            praes_conj_pass_3 = word[:-5] + 'ere'
            if praes_conj_pass_3 in comb:
                morf.write(comb[praes_conj_pass_3][:-3] + 'āntŭr' + '(III. Praes. Conj. Pass. 3Pl.)')

        elif word.endswith('rer'):
            if word[-4] == 'a':
                ipf_conj_pass_1 = word[:-3] + 're'
                if ipf_conj_pass_1 in comb:
                    morf.write(comb[ipf_conj_pass_1][:-3] + 'ārĕr' + '(I. Imperf. Conj. Pass. 1Sg.)')
            elif word[-4] == 'e':
                ipf_conj_pass = word[:-3] + 're'
                if ipf_conj_pass in comb:
                    morf.write(comb[ipf_conj_pass][:-3] + 'erĕr' + '(II./III. Imperf. Conj. Pass. 1Sg.)')
            elif word[-4] == 'i':
                ipf_conj_pass_4 = word[:-3] + 're'
                if ipf_conj_pass_4 in comb:
                    morf.write(comb[ipf_conj_pass_4][:-3] + 'īrĕr' + '(IV. Imperf. Conj. Pass. 1Sg.)')

        elif word.endswith('reris'):
            if word[-6] == 'a':
                ipf_conj_pass_1 = word[:-5] + 're'
                if ipf_conj_pass_1 in comb:
                    morf.write(comb[ipf_conj_pass_1][:-3] + 'ārērĭs' + '(I. Imperf. Conj. Pass. 2Sg.)')
            elif word[-6] == 'e':
                ipf_conj_pass = word[:-5] + 're'
                if ipf_conj_pass in comb:
                    morf.write(comb[ipf_conj_pass][:-3] + 'erērĭs' + '(II./III. Imperf. Conj. Pass. 2Sg.)')
            elif word[-6] == 'i':
                ipf_conj_pass_4 = word[:-5] + 're'
                if ipf_conj_pass_4 in comb:
                    morf.write(comb[ipf_conj_pass_4][:-3] + 'īrērĭs' + '(IV. Imperf. Conj. Pass. 2Sg.)')

        elif word.endswith('retur'):
            if word[-6] == 'a':
                ipf_conj_pass_1 = word[:-5] + 're'
                if ipf_conj_pass_1 in comb:
                    morf.write(comb[ipf_conj_pass_1][:-3] + 'ārētŭr' + '(I. Imperf. Conj. Pass. 3Sg.)')
            elif word[-6] == 'e':
                ipf_conj_pass = word[:-5] + 're'
                if ipf_conj_pass in comb:
                    morf.write(comb[ipf_conj_pass][:-3] + 'eretŭr' + '(II./III. Imperf. Conj. Pass. 3Sg.)')
            elif word[-6] == 'i':
                ipf_conj_pass_4 = word[:-5] + 're'
                if ipf_conj_pass_4 in comb:
                    morf.write(comb[ipf_conj_pass_4][:-3] + 'īrētŭr' + '(IV. Imperf. Conj. Pass. 3Sg.)')

        elif word.endswith('remur'):
            if word[-6] == 'a':
                ipf_conj_pass_1 = word[:-5] + 're'
                if ipf_conj_pass_1 in comb:
                    morf.write(comb[ipf_conj_pass_1][:-3] + 'ārēmŭr' + '(I. Imperf. Conj. Pass. 1Pl.)')
            elif word[-6] == 'e':
                ipf_conj_pass = word[:-5] + 're'
                if ipf_conj_pass in comb:
                    morf.write(comb[ipf_conj_pass][:-3] + 'erēmŭr' + '(II./III. Imperf. Conj. Pass. 1Pl.)')
            elif word[-6] == 'i':
                ipf_conj_pass_4 = word[:-5] + 're'
                if ipf_conj_pass_4 in comb:
                    morf.write(comb[ipf_conj_pass_4][:-3] + 'īrēmŭr' + '(IV. Imperf. Conj. Pass. 1Pl.)')

        elif word.endswith('remini'):
            if word[-6] == 'a':
                ipf_conj_pass_1 = word[:-6] + 're'
                if ipf_conj_pass_1 in comb:
                    morf.write(comb[ipf_conj_pass_1][:-3] + 'ārēmĭnī' + '(I. Imperf. Conj. Pass. 2Pl.)')
            elif word[-6] == 'e':
                ipf_conj_pass = word[:-6] + 're'
                if ipf_conj_pass in comb:
                    morf.write(comb[ipf_conj_pass][:-3] + 'erēmĭnī' + '(II./III. Imperf. Conj. Pass. 2Pl.)')
            elif word[-6] == 'i':
                ipf_conj_pass_4 = word[:-6] + 're'
                if ipf_conj_pass_4 in comb:
                    morf.write(comb[ipf_conj_pass_4][:-3] + 'īrēmĭnī' + '(IV. Imperf. Conj. Pass. 2Pl.)')

        elif word.endswith('rentur'):
            if word[-6] == 'a':
                ipf_conj_pass_1 = word[:-6] + 're'
                if ipf_conj_pass_1 in comb:
                    morf.write(comb[ipf_conj_pass_1][:-3] + 'ārēntŭr '+ '(I. Imperf. Conj. Pass. 2Pl.)')
            elif word[-6] == 'e':
                ipf_conj_pass = word[:-6] + 're'
                if ipf_conj_pass in comb:
                    morf.write(comb[ipf_conj_pass][:-3] + 'erentŭr' + '(II./III. Imperf. Conj. Pass. 2Pl.)')
            elif word[-6] == 'i':
                ipf_conj_pass_4 = word[:-6] + 're'
                if ipf_conj_pass_4 in comb:
                    morf.write(comb[ipf_conj_pass_4][:-3] + 'īrēntŭr' + '(IV. Imperf. Conj. Pass. 2Pl.)')

        elif word.endswith('vi'):
            if word[-3] == 'a':
                pf_act_1 = word[:-2] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + 'āvī' + '(I. Perf. Ind. Act.  1Sg.)')
            elif word[-3] == 'i':
                pf_act_3 = word[:-3] + 'ere'
                pf_act_4 = word[:-2] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + 'īvī' + '(III. Perf. Ind. Act. 1Sg.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvī' + '(IV. Perf. Ind. Act. 1Sg.)')
            elif word[-3] == 'e':
                pf_act = word[:-2] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + 'ēvī' + '(II./III. Perf. Ind. Act. 1Sg.)')
            elif word[-3] == 'o':
                pf_act_8 = word[:-3] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + 'ōvī' + '(II./III. Perf. Ind. Act. 1Sg.)')
                
        elif word.endswith('visti'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + 'āvĭstī' + '(I. Perf. Ind. Act. 2Sg.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + 'īvĭstī' + '(III. Perf. Ind. Act. 2Sg.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + 'īvĭstī' + '(IV. Perf. Ind. Act. 2Sg.)')
            elif word[-6] == 'e':
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + 'ēvĭstī' + '(II./III. Perf. Ind. Act. 2Sg.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + 'ōvĭstī' + '(II./III. Perf. Ind. Act. 2Sg.)')

        elif word.endswith('vit'):
            if word[-4] == 'a':
                pf_act_1 = word[:-3] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + 'āvĭt' + '(I. Perf. Ind. Act. 3Sg.)')
            elif word[-4] == 'i':
                pf_act_3 = word[:-4] + 'ere'
                pf_act_4 = word[:-3] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + 'īvĭt' + '(III. Perf. Ind. Act. 3Sg.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + 'īvĭt' + '(IV. Perf. Ind. Act. 3Sg.)')
            elif word[-4] == 'e':
                pf_act = word[:-3] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + 'ēvĭt' + '(II./III. Perf. Ind. Act. 3Sg.)')
            elif word[-4] == 'o':
                pf_act_8 = word[:-4] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + 'ōvĭt' + '(II./III. Perf. Ind. Act. 3Sg.)')

        elif word.endswith('vimus'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + 'āvĭmŭs' + '(I. Perf. Ind. Act. 1Pl.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + 'īvĭmŭs' + '(III. Perf. Ind. Act. 1Pl.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + 'īvĭmŭs' + '(IV. Perf. Ind. Act. 1Pl.)')
            elif word[-6] == 'e':
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + 'ēvĭmŭs' + '(II./III. Perf. Ind. Act. 1Pl.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + 'ōvĭmŭs' + '(II./III. Perf. Ind. Act. 1Pl.)')

        elif word.endswith('vistis'):
            if word[-7] == 'a':
                pf_act_1 = word[:-6] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + 'āvĭstĭs' + '(I. Perf. Ind. Act. 2Pl.)')
            elif word[-7] == 'i':
                pf_act_3 = word[:-7] + 'ere'
                pf_act_4 = word[:-6] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + 'īvĭstĭs' + '(III. Perf. Ind. Act. 2Pl.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + 'īvĭstĭs' + '(IV. Perf. Ind. Act. 2Pl.)')
            elif word[-7] == 'e':
                pf_act = word[:-6] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + 'ēvĭstĭs' + '(II./III. Perf. Ind. Act. 2Pl.)')
            elif word[-7] == 'o':
                pf_act_8 = word[:-7] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + 'ōvĭstĭs' + '(II./III. Perf. Ind. Act. 2Pl.)')

        elif word.endswith('verunt'):
            if word[-7] == 'a':
                pf_act_1 = word[:-6] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + 'āvērŭnt' + '(I. Perf. Ind. Act. 3Pl.)')
            elif word[-7] == 'i':
                pf_act_3 = word[:-7] + 'ere'
                pf_act_4 = word[:-6] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + 'īvērŭnt' + '(III. Perf. Ind. Act. 3Pl.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + 'īvērŭnt' + '(IV. Perf. Ind. Act. 3Pl.)')
            elif word[-7] == 'e':
                pf_act = word[:-6] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + 'ēvērŭnt' + '(II./III. Perf. Ind. Act. 3Pl.)')
            elif word[-7] == 'o':
                pf_act_8 = word[:-7] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + 'ōvērŭnt' + '(II./III. Perf. Ind. Act. 3Pl.)')

        elif word.endswith('irunt'):
            if word[-6] == 'u' or word[-6] == 's' or word[-6] == 'x' or word[-6] == 'i': #check!
                pf_act_1 = word[:-6] + 'are'
                pf_act = word[:-6] + 'ere'
                pf_act_4 = word[:-6] + 'ire'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + 'ŭīrŭnt' + '(I. Perf. Ind. Act. 3Pl.)')
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + 'ŭīrŭnt' + '(II./III. Perf. Ind. Act. 3Pl.)')
                if pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + 'ŭīrŭnt' + '(IV. Perf. Ind. Act. 3Pl.)')

        elif word.endswith('veram'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrăm' + ' (I. Plsqp. Ind. Act. 1Sg.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrăm' + ' (III. Plsqp. Ind. Act. 1Sg.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrăm' + ' (IV. Plsqp. Ind. Act. 1Sg.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrăm' + ' (II./III. Plsqp. Ind. Act. 1Sg.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrăm' + ' (II./III. Plsqp. Ind. Act. 1Sg.)')


        elif word.endswith('veras'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrās' + ' (I. Plsqp. Ind. Act. 2Sg.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrās' + ' (III. Plsqp. Ind. Act. 2Sg.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrās' + ' (IV. Plsqp. Ind. Act. 2Sg.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrās' + ' (II./III. Plsqp. Ind. Act. 2Sg.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrās' + ' (II./III. Plsqp. Ind. Act. 2Sg.)')

        elif word.endswith('verat'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrăt' + ' (I. Plsqp. Ind. Act. 3Sg.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrăt' + ' (III. Plsqp. Ind. Act. 3Sg.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrăt' + ' (IV. Plsqp. Ind. Act. 3Sg.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrăt' + ' (II./III. Plsqp. Ind. Act. 3Sg.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrăt' + ' (II./III. Plsqp. Ind. Act. 3Sg.)')

        elif word.endswith('veramus'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrāmŭs' + ' (I. Plsqp. Ind. Act. 1Pl.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrāmŭs' + ' (III. Plsqp. Ind. Act. 1Pl.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrāmŭs' + ' (IV. Plsqp. Ind. Act. 1Pl.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrāmŭs' + ' (II./III. Plsqp. Ind. Act. 1Pl.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrāmŭs' + ' (II./III. Plsqp. Ind. Act. 1Pl.)')

        elif word.endswith('veratis'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrātĭs' + ' (I. Plsqp. Ind. Act. 2Pl.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrātĭs' + ' (III. Plsqp. Ind. Act. 2Pl.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrātĭs' + ' (IV. Plsqp. Ind. Act. 2Pl.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrātĭs' + ' (II./III. Plsqp. Ind. Act. 2Pl.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrātĭs' + ' (II./III. Plsqp. Ind. Act. 2Pl.)')

        elif word.endswith('verant'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrănt' + ' (I. Plsqp. Ind. Act. 3Pl.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrănt' + ' (III. Plsqp. Ind. Act. 3Pl.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrănt' + ' (IV. Plsqp. Ind. Act. 3Pl.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrănt' + ' (II./III. Plsqp. Ind. Act. 3Pl.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrănt' + ' (II./III. Plsqp. Ind. Act. 3Pl.)')

        elif word.endswith('vero'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrŏ' + ' (I. Fut. II Act. 1Sg.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrŏ' + ' (III. Fut. II Act. 1Sg.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrŏ' + ' (IV. Fut. II Act. 1Sg.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrŏ' + ' (II./III. Fut. II Act. 1Sg.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrŏ' + ' (II./III. Fut. II Act. 1Sg.)')

        elif word.endswith('veris'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrĭs' + ' (I. Fut. II Act. 2Sg.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrĭs' + ' (III. Fut. II Act. 2Sg.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrĭs' + ' (IV. Fut. II Act. 2Sg.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrĭs' + ' (II./III. Fut. II Act. 2Sg.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrĭs' + ' (II./III. Fut. II Act. 2Sg.)')

        elif word.endswith('verit'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrĭt' + ' (I. Fut. II Act. 3Sg.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrĭt' + ' (III. Fut. II Act. 3Sg.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrĭt' + ' (IV. Fut. II Act. 3Sg.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrĭt' + ' (II./III. Fut. II Act. 3Sg.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrĭt' + ' (II./III. Fut. II Act. 3Sg.)')

        elif word.endswith('verimus'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrĭmŭs' + ' (I. Fut. II Act. 1Pl.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrĭmŭs' + ' (III. Fut. II Act. 1Pl.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrĭmŭs' + ' (IV. Fut. II Act. 1Pl.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrĭmŭs' + ' (II./III. Fut. II Act. 1Pl.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrĭmŭs' + ' (II./III. Fut. II Act. 1Pl.)')

        elif word.endswith('veritis'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrĭtĭs' + ' (I. Fut. II Act. 2Pl.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrĭtĭs' + ' (III. Fut. II Act. 2Pl.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrĭtĭs' + ' (IV. Fut. II Act. 2Pl.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrĭtĭs' + ' (II./III. Fut. II Act. 2Pl.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrĭtĭs' + ' (II./III. Fut. II Act. 2Pl.)')

        
        elif word.endswith('verint'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrĭnt' + ' (I. Fut. II Act. 3Pl.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrĭnt' + ' (III. Fut. II Act. 3Pl.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrĭnt' + ' (IV. Fut. II Act. 3Pl.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrĭnt' + ' (II./III. Fut. II Act. 3Pl.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrĭnt' + ' (II./III. Fut. II Act. 3Pl.)')

        elif word.endswith('verim'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrĭm' + ' (I. Fut. II Act. 1Sg.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrĭm' + ' (III. Fut. II Act. 1Sg.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrĭm' + ' (IV. Fut. II Act. 1Sg.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrĭm' + ' (II./III. Fut. II Act. 1Sg.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrĭm' + ' (II./III. Fut. II Act. 1Sg.)')

        elif word.endswith('verant'):
            if word[-6] == 'a':
                pf_act_1 = word[:-5] + 're'
                if pf_act_1 in comb:
                    morf.write(comb[pf_act_1][:-3] + u'āvĕrănt' + ' (I. Plsqp. Con. Act. 1Sg.)')
            elif word[-6] == 'i':
                pf_act_3 = word[:-6] + 'ere'
                pf_act_4 = word[:-5] + 're'
                if pf_act_3 in comb:
                    morf.write(comb[pf_act_3][:-3] + u'īvĕrănt' + ' (III. Plsqp. Con. Act. 1Sg.)')
                elif pf_act_4 in comb:
                    morf.write(comb[pf_act_4][:-3] + u'īvĕrănt' + ' (IV. Plsqp. Con. Act. 1Sg.)')
            elif word[-6] == 'e':                
                pf_act = word[:-5] + 're'
                if pf_act in comb:
                    morf.write(comb[pf_act][:-3] + u'ēvĕrănt' + ' (II./III. Plsqp. Con. Act. 1Sg.)')
            elif word[-6] == 'o':
                pf_act_8 = word[:-6] + 'ere'
                if pf_act_8 in comb:
                    morf.write(comb[pf_act_8][:-3] + u'ōvĕrănt' + ' (II./III. Plsqp. Con. Act. 1Sg.)')       
                    
            elif word.endswith('ta'):
                verb_2l = word[:-2] + 're'
                if verb_2l in comb:
                    if text[number+1] == 'sim':
                        morf.write(comb[verb_2l][:-2] +  'tă' + 'sĭm' + ';' + 'Perf. Con. Pass.1Sg.' )
                    elif text[number+1] == 'sis':
                        morf.write(comb[verb_2l][:-2] +  'tă' + 'sīs' + ';' + 'Perf. Con. Pass.2Sg.' )
                    elif text[number+1] == 'sit':
                        morf.write(comb[verb_2l][:-2] +  'tă' + 'sĭt' + ';' + 'Perf. Con. Pass.3Sg.' )
                    elif text[number+1] == 'simus':
                        morf.write(comb[verb_3l][:-2] +  'tă' + ' sīmus' + ';' + 'Perf. Con. Pass.1Pl.' )
                    elif text[number+1] == 'sitis':
                        morf.write(comb[verb_3l][:-2] +  'tă' + ' sītĭs' + ';' + 'Perf. Con. Pass.2Pl.' )
                    elif text[number+1] == 'sint':
                        morf.write(comb[verb_3l][:-2] +  'tă' + ' sĭnt' + ';' + 'Perf. Con. Pass.3Pl.' )

            elif word.endswith('tum'):
                verb_3l = word[:-3] + 're'
                if verb_3l in comb:
                    if text[number+1] == 'sim':
                        morf.write(comb[verb_3l][:-2] +  'tŭm' + 'sĭm' + ';' + 'Perf. Con. Pass.1Sg.' )
                    elif text[number+1] == 'sis':
                        morf.write(comb[verb_3l][:-2] +  'tŭm' + 'sīs' + ';' + 'Perf. Con. Pass.2Sg.' )
                    elif text[number+1] == 'sit':
                        morf.write(comb[verb_3l][:-2] +  'tŭm' + 'sĭt' + ';' + 'Perf. Con. Pass.3Sg.' )

            elif word.endswith('tus'):
                verb_3l = word[:-3] + 're'
                if verb_3l in comb:
                    if text[number+1] == 'sim':
                        morf.write(comb[verb_3l][:-2] +  'tŭs' + 'sĭm' + ';' + 'Perf. Con. Pass.1Sg.' )
                    elif text[number+1] == 'sis':
                        morf.write(comb[verb_3l][:-2] +  'tŭs' + 'sīs' + ';' + 'Perf. Con. Pass.2Sg.' )
                    elif text[number+1] == 'sit':
                        morf.write(comb[verb_3l][:-2] +  'tŭs' + 'sĭt' + ';' + 'Perf. Con. Pass.3Sg.' )

            elif word.endswith('tae'):
                verb_3l = word[:-3] + 're'
                if verb_3l in comb:
                    if text[number+1] == 'simus':
                        morf.write(comb[verb_3l][:-2] +  'tăĕ' + ' sīmus' + ';' + 'Perf. Con. Pass.1Pl.' )
                    elif text[number+1] == 'sitis':
                        morf.write(comb[verb_3l][:-2] +  'tăĕ' + ' sītĭs' + ';' + 'Perf. Con. Pass.2Pl.' )
                    elif text[number+1] == 'sint':
                        morf.write(comb[verb_3l][:-2] +  'tăĕ' + ' sĭnt' + ';' + 'Perf. Con. Pass.3Pl.' )

            elif word.endswith('ti'):
                verb_2l = word[:-2] + 're'
                if verb_2l in comb:                        
                    if text[number+1] == 'simus':
                        morf.write(comb[verb_2l][:-2] +  'tī' + ' sīmus' + ';' + 'Perf. Con. Pass.1Pl.' )
                    elif text[number+1] == 'sitis':
                        morf.write(comb[verb_2l][:-2] +  'tī' + ' sītĭs' + ';' + 'Perf. Con. Pass.2Pl.' )
                    elif text[number+1] == 'sint':
                        morf.write(comb[verb_2l][:-2] +  'tī' + ' sĭnt' + ';' + 'Perf. Con. Pass.3Pl.' )


                    elif text[number+1] == 'eram':                    
                        morf.write(comb[word] +  'tae' + ' eram' + ';' + 'Plūsquampf. In.P. 1Sg.' )
                    elif text[number+1] == 'eras':                    
                        morf.write(comb[word] +  'tae' + ' erās' + ';' + 'Plūsquampf. In.P. 2Sg.' )
                    elif text[number+1] == 'erat':                    
                        morf.write(comb[word] +  'tae' + ' erat' + ';' + 'Plūsquampf. In.P. 3Sg.' )

                    elif text[number+1] == 'ero':                    
                        morf.write(comb[word] +  'tae' + ' ero' + ';' + 'Futūrum II Pass. 1Sg.' )
                    elif text[number+1] == 'eris':                    
                        morf.write(comb[word] +  'tae' + ' eris' + ';' + 'Futūrum II Pass. 2Sg.' )
                    elif text[number+1] == 'erit':                    
                        morf.write(comb[word] +  'tae' + ' erit' + ';' + 'Futūrum II Pass. 3Sg.' )
 

                    if text[number+1] == 'sumus':                    
                        morf.write(comb[word_vb][:-2] +  'tae' + ' sumus' + ';' + 'Perf. Ind. Pass.1Pl.' )
                    elif text[number+1] == 'estis':                    
                        morf.write(comb[word_vb][:-2] +  'tae' + ' estis' + ';' + 'Perf. Ind. Pass.2Pl.' )
                    elif text[number+1] == 'sunt':                    
                        morf.write(comb[word_vb][:-2] +  'tae' + ' sunt' + ';' + 'Perf. Ind. Pass.3pl.' )
                        
                    elif text[number+1] == 'eramus':                    
                        morf.write(comb[word_vb][:-2] +  'tae' + ' erāmus' + ';' + 'Plūsquampf. Ind. Pass.1Pl.' )
                    elif text[number+1] == 'eratis':                    
                        morf.write(comb[word_vb][:-2] +  'tae' + ' erātis' + ';' + 'Plūsquampf. Ind. Pass.2Pl.' )
                    elif text[number+1] == 'erant':                    
                        morf.write(comb[word_vb][:-2] +  'tae' + ' erant' + ';' + 'Plūsquampf. Ind. Pass.3Pl.' )
                        
                    elif text[number+1] == 'erimus':                    
                        morf.write(comb[word_vb][:-2] +  'tae' + ' erimus' + ';' + 'Futūrum II Pass.1Pl.' )
                    elif text[number+1] == 'eritis':                    
                        morf.write(comb[word_vb][:-2] +  'tae' + ' eritis' + ';' + 'Futūrum II Pass.2Pl.' )
                    elif text[number+1] == 'eramus':                    
                        morf.write(comb[word_vb][:-2] +  'tae' + ' erunt' + ';' + 'Futūrum II Pass.3Pl.' )

                    elif text[number+1] == 'essemus':                    
                        morf.write(comb[word_vb][:-2] +  'ae' + ' essēmus' + ';' + 'Plsqpf. Coni.Pass.1Pl.' )
                    elif text[number+1] == 'essetis':                    
                        morf.write(comb[word_vb][:-2] +  'ae' + ' essētis' + ';' + 'Plsqpf. Coni. Pass.2Pl.' )
                    elif text[number+1] == 'essent':                    
                        morf.write(comb[word_vb][:-2] +  'ae' + ' essent' + ';' + 'Plsqpf. Coni. Pass.3Pl.' )                

    else:
        morf.write(word + '\n')
        notFoundWords += 1
print notFoundWords
foundWords = len(text) - notFoundWords
print foundWords
print  len(text)
percentOfFoundWords = foundWords / (len(text) / 100.00000)     
morf.write('Percent of found words: ' + str(percentOfFoundWords)  + '%')

        
d.close()            
g.close()
f.close()

            
        
            

            
            
        
