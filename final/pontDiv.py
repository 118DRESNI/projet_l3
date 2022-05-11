#     +------------+
#     |            |
#     |          +-+-+
#     |          |   |
#     |          |   |
#     |          |R1 |
#     |          |   |
#     |          |   |
#     |          +-+-+
#     |            |
#     |            |
#     |            |
#     |            |
#  ---+---         |
#         5V       |     ^
#    -+-         #####   |
#     |          #   #   |
#     |          #   #   |
#     |          #R2 #   | Ur2
#     |          #   #   |
#     |          #   #   |
#     |          #####   |
#     |            |     |
#     |            |     |
#     |            |
#     +------------+

# programme calculant la réistance R2 selon R1, Ur2 et VCC
VCC = 5
R1 = 1000
Ur2 = 0

def pontDiv (Ur2):
	num = -(R1 * Ur2)
	den = Ur2 - VCC
	R2 = num /den
	return R2

#test
#R2 = round(pontDiv(3.45),3)
#print (R2)
