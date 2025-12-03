from distutils.command.build_scripts import first_line_re


data = "1-14,46452718-46482242,16-35,92506028-92574540,1515128146-1515174322,56453-79759,74-94,798-971,49-66,601-752,3428-4981,511505-565011,421819-510058,877942-901121,39978-50500,9494916094-9494978970,7432846301-7432888696,204-252,908772-990423,21425-25165,1030-1285,7685-9644,419-568,474396757-474518094,5252506279-5252546898,4399342-4505058,311262290-311393585,1895-2772,110695-150992,567521-773338,277531-375437,284-364,217936-270837,3365257-3426031,29828-36350"


### loop through list of lists, count list[list[i]] and if first half matches second half total +=? 

def part_one():
    ranges_list = []
    total = 0

    for i in data.split(","):
        start, end = i.split('-')
        ranges_list.append(list(range(int(start), int(end) + 1)))

    print(ranges_list[0])
    for i in ranges_list:
        for x in i:
            string_num = str(x)
            prodID_len = len(string_num)

            if prodID_len % 2 == 0:
                prodID_half_len = prodID_len // 2
                first_half = string_num[0:prodID_half_len]
                last_half = string_num[prodID_half_len + (prodID_len%2) : prodID_len]

                if first_half == last_half:
                    total += x
                    print("First Half: " + first_half)
                    print("Last Half: " + last_half)

    print(total)

