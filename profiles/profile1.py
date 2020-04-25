import cProfile
from vigenere_cracker import find_key_len

cypher = '1f0c000d0a1c0200020a070415170a120b18000d0c0011150a1c1c030e17011d0e181f02111301111d0b1c110611111d1b1c14000200111b0e161e070206111c080a03170613011b0b0d1b00001d171b0318050c1107161904171d00101d1115021f150c001b04181e1516040d17011b03181f0a00130917021403040d0b1613011611040f110a1a031c10110a1d0b071916120c111e0c1219181004001a001b0b14121608010306021412060b1b0b111e1c150400060a06141b120608060a00051c001102060012020b17000f1b13111f00070d0a01121108120404101a0c1a0a0d1c0b1006040008090617001a0407081d100a17060a1a1e0e120710140a060e16010a0d13131d1f0c0011060111071918180c0d150406040a1807061104011e1c070d0602171b090c10110f1d0615191c17071a1d0312041a1a040f010d151e171c111a171116081c1d041302171b1b1c17071a060d110b161c01021c01101f0c1404071f0c1a040a071702060c1b030d1b0010060400081000040f010a16080d070c0d15111c0c0d121606131100011c11041017011b180d170a0c0002110c0b100a0e02041a14121d0a141c031b1f1007160113061f1d18100e10130b101d18010e02010615030b16060c1c031d0a0c01000a06161b1d1c0104171b0a1a1e0d1c15111d01010e1c1d5c560000071d100104171d17070c171706021e0c12020b1d0c021306000417140410130b1519101c0b1006040008101d110b17121b1f1d000a05060d110a160500111c0a060f1c14040d10100d041714575342081d01151a0a0d1f0407060a0300111f0a1a1911070a101a0a06080c031616021518041c000c0d060d15190a07041717041a09091c11061c111d0c151f1c0211171b1e0a070d06110a01030d011c021600181e1c040d06000007021416020c04000603160116021c01180c0e1e04081717070518050014131117051c170c0d160c070f1c1f0c061404071911161c0b1313111e1606020b06111b0e151c1606160015010a1c0b130000170416061610071504011016160c1c090d19161b041517111c081f1601060004180a160500111c0811030d00120c1d151d030d1c15111700191d0d070d061317060c1714000e170b001e1615030a110c15010a1a0b0c1c00071918070002000007020e1c17111b00100c1b1c1017060d1d1e091c16101b071d0110071c171a04001911161c020000170217000c0717171d031e170c100204000e111a0b041e0a170c15030a0f1b0611020b1613061c111c081712110a1d0b15011e06041116111b0a0b16001706121b0e11121717171711091f1601060a15180c17161610110d11090c1f0007060a151f0b1a13061b0b00051c1d001b0612110812040c171a081d01151a0a0d010a120018000e1014171b001a1b0c0d1304170e1601010a1c02000209160a131e00120c141a090a131703040d1b110b1715180c171d0c0d15111c080a1615061d1518080e1b0a10020a1f08161d110b17061b031d1a110a1d0b1b0b181d0a0d0b081d1900121608170100051807110b170c061e0d1211061c0a000f1c1a01061c111d0b101601171d0402021017030f13021304171403061600060c151c03051b061d0c1500110c060d11040b000d0a020811030d1216171a00001f0c1e150216081d031000111113111d02171216100708111e0e1b0417060d111d0b16160a16001a1911121600130918081d120702110e011d0b1c09061b0b10040a07170a1010000417141616021518041c00110c140c13050d070d0602041a091c1e0c00011115191c140a1517171a001c1d11101317111918180c0d15000c190b120a11160c1a0c0b0a040d160a12191c1d100d1d17000516170a1b0111111d0a070a001d0804080d160c0d130b1d031a010002010c1a0a150a061606111c1f161211041e0a160c151e04111900001d15120606130107041e1d1013140a06020c01060c000a1a0c0f1a171601100409180700101c00031e15161117171700020d01040019111c081606110100001506181f0910060a06041c00090a1c0e1109101d110b170b111a0a1f00170600060c0b1603111700000218100606011600051c010010070900040a12150206061c1a16010e021c011b0b0d160b001a041b19101016000004190f1516030c00021b021d00150a06111d031e0011020600070c1e120c0d0111110c1a1b0a171a00060c17170a0506001a0c1e120c0d01111b19111617001d101a190b1a00101d17111b1c1d110b1710070a160500111c0811030d04001117011b041714120b1311111b1c011c0c1c0011010a160c10160a1d031e1c0d0a1d021b1b141a0e061600030417161710130c100417120b0a1c11111f0f1a00140b0a011b1c140a174755071918070010130b1019111603061600060c15140a1517171a001c1d11021e09170518000c0d15111c080a120806110a191d181d0c06010c001e1a0104190b161b0c0b1a0b0402171d0e1c000d02040018081f0716171311111e1807110a1f0007191603041a071500024843110a1f00071911160b0c0008150109010c00171612020b10001106041d031e1c0a070104170e1601010a1c0200021615030a110c15010a15170c1f0801010d1a150f1716000c0d16160613111d031e1212020b04000e18000d111716111f0f1616021c01180c001a0b04060d110b16060b0713111d0217150a1113031d1e1a12090000101a0e11070d020616111b1c01040f150a02080b1d0a110107110110161306050c18010b1614161b17110b1c1700111309160c101f0a1606160304171703021e09071e16150411150a180c0b14000f0b111b0b1601000a150b17021403040d1b0007191112110e130e111911160012070c04001c1d11021e0a1a0a0e1a110b060d1d1f1d030411061c161f1618001101111c0c0d1c0317170b1c081503060c1c0b110e0d0011020600071a10070d0e130b010b181011160000061e181d01171a001a0a1c0704000711150e1a1c17071b0b13191600110206001b0b1f1a060a1309070c17170716010c1a080a0015061d1518081817120c00171d081d12070c071118020a1a0b04020a000817070c021e01110c150016171311110a160500111c0811030d000d02040000020a00000713161d091c1f0a0d1516000c17170c0d1515011f1a1b04101b0b131f0c1f001013071b180d1b0a14060a071d1c1d0117131d040c0016170e1d0b111416150306000c1a0a1f060b070110040b0b1c0b17140a060808060c131f001a191b16030c00001d191d1a16020215110c0b00020c04000603160116021c01000209120c071716151f1c0015061c011d031e1b0a1600161b030d1b00131a0a1a0811060b171b0b130b160103111b001a090a01000f13111d1b1c000a05130c10080a1c170c060d111f091617101d0b15011a1c0b0d17060004161d16171a04000010140d17150c02080d1b000e130b11091e161106130807021f00000d1b0a061e0d121106130c10080a2067120b1d0c1a03160108021e111d001c000a15171707081c1a16100700071e0c100d020106180414121106110d15031e16040d160d110c15070d131d091d0e002067160a060c1a0e161d030600001a0e1c010a0c1f1615031d110c0713091809180a110b1703060817091c0a1c131d191c00110b17151b191c1d110a130912020b1517020701150e1a1c17071b0b13191600001517171501181a010601111b0a160500111c0a061e0e1a110b1d0312041a1a040f010c1a031c040f0600161114101f090a1c0a1d1e1412161013061c180a16111701061b03171606171b060119181d011413161c041714110c1c16000c0d16040f1e161514101d02171a000d051805000117001a0417060b07131111090e1a110b020c000e11161605000a19011018000f0b16170c141217171b16001e161b0c0c150a02001018000717121d031c1f0005060a1c0416170013131700001c1d110c140d110c15070d071b17110e0d1c17021f1c150e0d1c0b021c0118191e1c13091d0b1c180a070007131706040f16030c0004100c101f1c16020115191c1c0b171a00071918070010110a06021712130a0010071f1c00150c1c16110c0d070d061d0d1d020a070417170d1b180a160c0d110a1818141110101e040719141c0b171a0a1c0416140a151f0c1f081d16120a1c0018081f070a0b1b0a1008091217171f001a1916150d06130900051d1a170611111b1f181e1c0211111b03181d010f06021b1b131c0b0b071600081d1217111b13110b16010407130c18140c03010206001b030d1b0010060400080a100a111d0b151b100110100000071d161d1606131100051c1c0d0a1d16000c0d160d0c0716110417100a0f070816180a1f041006081b030d1b0f0c010d010c18110c001900180e161f100e101007091000150206061c0c091b000f0203060214070d06140010080b1209041d13111f171e000d060c070417100a0d010c07191c1d11141b111c1e161e00041d13111f171c17101a04020417140916110e03020b180c0d15121d1911070d061b1706081e1a0a0d130910040b1606171d17070b0b1c08171a0012081d1617021e0019080b14000d111c190c171202061f001a191814000d111c1b1911161710140c1a09101d02021c0c1a1a10070d09131711091206160b1c00060c0e1b0c17170d1b180a160407040c07080b120b07060d111d0b16160a16001a190a000a0d1b0b180c0e120b07010a19081803150613091d031e170c111706000100070a13000007041d160b17'

cProfile.run('find_key_len(cypher)')
