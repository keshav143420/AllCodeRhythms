import unittest

import hackerearth.algorithms.linear_search.holiday_season as hs


class HolidaySeasonTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.hs = hs.HolidaySeason()

    def test_num_of_sub_sequences_sample_data(self):
        num_ele_in_seq = 5
        sequence = 'ababa'
        actual_result = self.hs.num_of_sub_sequences(num_ele_in_seq, sequence)
        expected_result = 2
        self.assertEqual(expected_result, actual_result)

    def test_num_of_sub_sequences_edge_case(self):
        num_ele_in_seq = 1
        sequence = 'a'
        actual_result = self.hs.num_of_sub_sequences(num_ele_in_seq, sequence)
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

    def test_num_of_sub_sequences_custom_case(self):
        num_ele_in_seq = 6
        sequence = 'aaaaaa'
        actual_result = self.hs.num_of_sub_sequences(num_ele_in_seq, sequence)
        expected_result = 15
        self.assertEqual(expected_result, actual_result)

    def test_num_of_sub_sequences_negative_case(self):
        num_ele_in_seq = 6
        sequence = 'abcdef'
        actual_result = self.hs.num_of_sub_sequences(num_ele_in_seq, sequence)
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

    def test_num_of_sub_sequences_judge_data_case(self):
        num_ele_in_seq = 34
        sequence = 'hylobclddzflmzitrxwwsqhozvgexhxjmm'

        actual_result = self.hs.num_of_sub_sequences(num_ele_in_seq, sequence)
        expected_result = 36
        self.assertEqual(expected_result, actual_result)

        num_ele_in_seq = 2000
        sequence = 'gbgipsvukgylwfyulteaucqtguivpdihgbzehwwezdaudbqgfasecqxduwskeldaamuiovnkdus' \
                   'ufmkfbznsmvqdcwhebitrhgtiecmifuwiflogwtfszpnnycixsygncmgsrmvnzlljewwakqxmjp' \
                   'ydyvyibtbvjaymglcjbmkjydrbrkizzllpkprfwiaixokiwxkslioijcqdqmmbjpkmuuriknfbu' \
                   'kkmunddzlgnqffrtbxmtnhhftsrptfzaqmnkouflnrzemktwrhvtlbygxjgkrlvgevkecoeknes' \
                   'jcijnopfjzhtzinftggjxdgfnlrraltmbjjjuxyubwfxyerrepuadvboaevxmpjktpsndzsfscy' \
                   'pusrapdrkkgwyrwfekxipcdyxbgyuquuxcxlxsztpnhylalrichqteabmusrtnkdrungklppwtv' \
                   'jyawzjencxrilghozdkimsqvqzpxmaceesbnxekqnvekbknpcnaucdbdugqymjbdsziyjguuzpo' \
                   'kalwhkyvijoctnxxzkhgzljointdgvqnygvemuvmsrhbglqheolvithnmqgfzhnnmraorxhfvzh' \
                   'cfyggzgujqnztyoryfxwxiinytvrcfoimjplqlhunpwyleqcvoexamsiymfdefkpshcobwihhmo' \
                   'nyfhhnzzjelhfwgmcoerbwccvqrsalcrxmszwuitdhdrcmmcelgucehsgktnqlhyxhfirdsjnii' \
                   'zbuvfxtbwefwffdgdhncoipsgxzmsvqvhgvjzcabrsjemmsgiarqnlhqykihdmfzmirmvuwtdpv' \
                   'hwhicfhezlyykdkyairtozrzholguvzohahffdyebtnnqpyzycwlnhmafiubmkaanswbremrket' \
                   'amztqohraevumoshjaindgcvgsfaorewftsncqbrudgrpabgrbevwuzyxzokkzpnpuyzbarjqor' \
                   'xwwrihxwuauvjvonkdamjfwpgyfmfmfwgjxowluaafidsqssbdjasdgecvxudkwjfwhcnqbpkds' \
                   'crdarmnursrzpvmnmkvixrpsyplwqlfncufnwserrkkeytniuzkrvfehjaztxjgcncgossyobjq' \
                   'lfdkwyupxdjzhvalagyyfglsapztvmzahuupfxpqfpvjgxakrkrxqjagmtsmisujobwnlonkuug' \
                   'awsljssisygmqurdsqdcxkdoorfdcqaatukrmgwkwcrlgsytvxiaykmopqutocmuzezwoxikvte' \
                   'vkhsgmkurnvdcafhfwihvijpzlksthvhegcwonrfqplbuhiwejyxvugdprqugxwxtmfmsaenrae' \
                   'cqsjbnyceuaxowzfyeiwpflsqtajfwezomrlrgjqlwguediraoqunihoyhmskylxvrqacrqolgt' \
                   'gokcsrcbtjlpvweafwlecqxqtancdonogzjibeiovmlniybunficmcarrwnedwkoupeqttlkmmy' \
                   'fczjeqagqsszvktzskopscgfukzolbigrnxcmtuvwzmnviplynnotxwqclypbfvfjzxokwtfqzq' \
                   'sgqymfpzkxyouoxuszebkzjlebphhnghpuivbimwbbvplsqaortycmwrjdivqabdeycpcdpzymi' \
                   'jjbkloyepriikpqjkyjhzpnakhwaerqhprfwzkxhecydpzxaotskzcnwjhejytrigkogkggnlwu' \
                   'mlzrsriakvjaqetaqgbqpmmtofpxfiblnqzcvohfatuafdbarjuxkpchmjrdfbdkxeuijqakvfw' \
                   'gnajmycxnsducoyvnrmgkllvotdlwvnfrpluwmivxuludcgigvyjmecgretwfiimxqyxsvguaiw' \
                   'jmxgonthtjpyzfopnrlcpvmmogfsjbasaznvhfhwcfztjfowrtraavbljqjgnpherzntanqmjpp' \
                   'qvhtctuyhyngjnhsdajgjwbpfyxktlgvdejtlhcfvqdqbfuqwy'
        actual_result = self.hs.num_of_sub_sequences(num_ele_in_seq, sequence)
        expected_result = 979714091
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
