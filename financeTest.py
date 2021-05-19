import numpy_financial as np
while True:

    print("Problem type")
    print("1. NPV (WACC + CFs")
    print("2. IRR")
    print("3. Initial Value and NPV")
    print("4. MIRR")
    print("5. Payback and Discounted Payback")
    print("6. NPV and Payback Period")
    print("7. Constant Growth Stock price given D1")
    print("8. Rate of Return and P1 given D0 and P0")
    print("9. Unevent Discounted Dividends")
    print("10 Constant Growth Stock Dividend given D0")
    print("11. Dividend yield with D1, g, and P0")
    print("12. Expected Total returns with D1, g, and P0") 
    print("13. Expected stock price given d0, rs, g")   
    print("14. D1 given d0, rs, g")  
    print("15. Value lost by choosing IRR over NPV")  
    print("16. Current market value with nonconstant growth given return, D0") 
    print("17. Dividend yield with D0, g, and P0")
    print("18. Preferred Stock Price given annual dividend, rate")
    print("19. Preferred Stock dividend given price, rate")
    print("20. Preferred Stock rate of return given annual dividend, price")
    print("21. Growth rate g given D1, price, rate of return")
    print("22. Dividends")
    print("23. Price in x years given current price, g, rate of return")
    print("24. Price given D1, g, beta, MRP, Risk Free Rate")
    print("25. Downsizing")
    problemType = input("Select problem type (q to quit): ")
    

    if problemType == 'q':
        break
    elif problemType == "1":
        numYears = int(input("Number of years: "))
        rate = float(input('WACC: ')) / 100
        CFs = []
        for i in range(0,numYears+1):
            CFs.append(int(input("CF: ")))

        NPV = 0
        for i in range(0,numYears+1):
            NPV += CFs[i]/pow(1+rate,i)
        print("NPV: %f" % NPV)

    elif problemType == '2':
        numYears = int(input("Number of years: "))
        CFs = []
        for i in range(0,numYears+1):
            CFs.append(int(input("CF: ")))

        IRR = np.irr(CFs) * 100
        print("IRR: %f" % IRR)
        

    elif problemType == '3':
        numYears = int(input("Number of years: "))
        IRR = float(input("IRR: ")) / 100
        WACC = float(input("WACC: ")) / 100
        CFs = []
        NCFs = []
        for i in range(0,numYears):
            CFs.append(int(input("CF: ")))

        Initial = 0
        for i in range(0,numYears):
            Initial += CFs[i]/pow(1+IRR,i+1)
        print("Initial: %f" % Initial)
        NCFs.append(-Initial)
        for i in range(0,numYears):
            NCFs.append(CFs[i])

        NPV = 0
        for i in range(0,numYears+1):
            NPV += NCFs[i]/pow(1+WACC,i)
        print("NPV: %f" % NPV)

    elif problemType == '4':
        numYears = int(input("Number of years: "))
        finRate = float(input("Finance Rate (WACC): ")) / 100
        invRate = float(input("Reinvestment Rate (WACC): ")) / 100
        CFs = []
        for i in range(0,numYears+1):
            CFs.append(int(input("CF: ")))

        MIRR = np.mirr(CFs,finRate, invRate) * 100
        print("MIRR: %f" % MIRR)
    elif problemType =='5':
        numYears = int(input("Number of years: "))
        discountedRate = float(input("Discounted Rate: ")) / 100
        CFs = []
        for i in range(0,numYears+1):
            CFs.append(int(input("CF: ")))
        
        cumCF = CFs[0]
        paybackPeriod = 0.000
        for i in range(1, numYears+1):
            cumCF += CFs[i]
            if cumCF >= 0:
                paybackPeriod += -((cumCF - CFs[i]) / CFs[i])
                for j in range(i+1,numYears+1):
                    cumCF += CFs[j]
                break
            if cumCF < 0:
                paybackPeriod += 1
        print("Payback Period: %f" % paybackPeriod)
        print("Unaccounted for Value: %f" % cumCF)

        DCF = []
        for i in range(numYears+1):
            DCF.append(CFs[i]/pow(1+discountedRate,i))
        CDCF = DCF[0]
        dPaybackPeriod = 0.000
        for i in range(1, numYears+1):
            CDCF += DCF[i]
            if CDCF >= 0:
                dPaybackPeriod += -((CDCF - DCF[i]) / DCF[i])
                for j in range(i+1,numYears+1):
                    CDCF += DCF[j]
                break
            if CDCF < 0:
                dPaybackPeriod += 1
        print("Discounted Payback Period: %f" % dPaybackPeriod)
        print("Discounted Unaccounted for Value: %f" % CDCF)

    elif problemType == '6':
        numYears = int(input("Number of years: "))
        paybackPeriod = float(input("Payback Period: "))
        WACC = float(input("WACC: ")) / 100
        CFs = []
        for i in range(0,numYears):
            CFs.append(int(input("CF: ")))
        
        Initial = 0
        count = 1
        while paybackPeriod >= count:
            Initial += CFs[count-1]
            count += 1
        decimal = paybackPeriod - count
        if decimal != 0:
            Initial += -decimal * CFs[count - 1]
        print("Initial Value: %f" % Initial)

        NCFs = []
        NCFs.append(-Initial)
        for i in range(0,numYears):
            NCFs.append(CFs[i])

        NPV = 0
        for i in range(0,numYears+1):
            NPV += NCFs[i]/pow(1+WACC,i)
        print(NPV)

    elif problemType == '7':
        d1 = float(input("D1: "))
        g = float(input("Growth Rate g: ")) / 100
        rs = float(input("Expected Rate of Return (rs): ")) / 100

        p0 = d1/(rs-g)
        print("P0: %f" % p0)
    
    elif problemType == '8':
        p0 = float(input("P0: "))
        d0 = float(input("D0: "))
        g = float(input("Growth Rate g: ")) / 100

        p1 = p0 * (1 + g)
        d1 = d0 * (1 + g)

        rs = d1 / p0 + g
        print("P1: %f" % p1)
        print("rs: %f" % rs)

    elif problemType == '9':
        numYears = int(input("Num Years: "))
        d0 = float(input("D0: "))
        g = float(input("Growth Rate g: ")) / 100
        whenChange = int(input("When does g change: "))
        newG = float(input("New Growth Rate g: ")) / 100

        dividends = []
        dividends.append(d0)

        for i in range(1,whenChange+1):
            dividends.append(d0 * pow(1 + g, i))
            print(dividends)
        
        count = 1
        for i in range(whenChange + 1, numYears+1):
            dividends.append(dividends[whenChange] * pow(1 + newG, count))
            count += 1
            
        for i in range(0, numYears+1):
            print("D: %f" % dividends[i])

    elif problemType == '10':
        d0 = float(input("D0: "))
        rs = float(input("Rs: ")) / 100
        g = float(input("Growth Rate g: ")) / 100

        d1 = d0 * (1 + g)
        p0 = d1/(rs-g) 
        print("P0: %f" % p0)

    elif problemType == '11':
        p0 = float(input("P0: "))
        d1 = float(input("D1: "))
        g = float(input("Growth Rate g: ")) / 100

        #d1= d0 * (1+g)

        DY = d1/p0 * 100

        print("DY: %f" % DY)

    elif problemType == '12':
        p0 = float(input("P0: "))
        d1 = float(input("D1: "))
        g = float(input("Growth Rate g: ")) / 100
        p1 = p0 * (1 + g)

        DY = d1/p0 * 100
        CGY = (p1 - p0) / p0 * 100

        print("CGY: %f" % CGY)
        print("DY: %f" % DY)

        TotalReturns = DY + CGY
        print("Rs: %f" % TotalReturns)

    elif problemType == '13':
        d0 = float(input("D0: "))
        rs = float(input("Rs: ")) / 100
        g = float(input("Growth Rate g: ")) / 100

        d1 = d0 * (1 + g)
        p0 = d1/(rs-g)
        print("P0: %f" % p0)

    elif problemType == '14':
        p0 = float(input("P0: "))
        rs = float(input("Rs: ")) / 100
        g = float(input("Growth Rate g: ")) / 100

        d1 = p0 * (rs - g)
        print(d1)

    elif problemType == '15':
        numYears = int(input("Number of years: "))
        rate = float(input('Rate: ')) / 100
        CFs1 = []
        CFs2 = []
        for i in range(0,numYears+1):
            CFs1.append(int(input("Company1 CF: ")))
        
        for i in range(0,numYears+1):
            CFs2.append(int(input("Company2 CF: ")))

        NPV1 = 0
        NPV2 = 0
        for i in range(0,numYears+1):
            NPV1 += CFs1[i]/pow(1+rate,i)
            NPV2 += CFs2[i]/pow(1+rate,i)

        IRR1 = np.irr(CFs1) * 100
        IRR2 = np.irr(CFs2) * 100

        print(f"\nCompany 1: NPV = %f, IRR = %f" % (NPV1, IRR1))
        print(f"Company 2: NPV = %f, IRR = %f" % (NPV2, IRR2))

        if IRR1 > IRR2 and NPV1 > NPV2:
            print(f"Noting forgone, gain of: %f" % (NPV1 - NPV2))
        elif IRR1 > IRR2 and NPV2 > NPV1:
            print(f"value forgone: %f" % (NPV2 - NPV1))
        elif IRR2 > IRR1 and NPV2 > NPV1:
            print(f"Noting forgone, gain of: %f" % (NPV2 - NPV1))
        elif IRR2 > IRR1 and NPV1 > NPV2:
            print(f"value forgone: %f" % (NPV1 - NPV2))
        else:
            print("Values equal, nothing forgone")
        
    elif problemType == '16':
        numYears = int(input("Number of years until constant: "))
        rate = float(input('Rate of return: ')) / 100
        D0 = float(input('D0: '))
        growthRates = []
        price = []

        for i in range(0,numYears):
            growthRates.append(float(input("growth rate in year %i: " % i))/100)
        
        dividends = []
        for i in range(0, numYears):
            if i == 0:
                dividends.append(D0 + D0 * growthRates[0])
            else:
                dividends.append(dividends[i-1] + dividends[i-1] * growthRates[i])
        print(dividends)

        lastPrice = dividends[-1] / (rate - growthRates[-1])
        print(lastPrice)

        currentPrice = 0
        for i in range(0, numYears - 1):
            currentPrice += dividends[i]/pow(1+rate, i+1)
            if i == numYears - 2:
                currentPrice += lastPrice/pow(1+rate, i+1)
        print("current price: %f" % currentPrice)
        
    elif problemType == '17':
        p0 = float(input("P0: "))
        d0 = float(input("D0: "))
        g = float(input("Growth Rate g: ")) / 100

        d1= d0 * (1+g)

        DY = d1/p0 * 100

        print("DY: %f" % DY)
    
    elif problemType == '18':
        rate = float(input("Rate of return: "))/100
        d0 = float(input("Annual Dividend: "))

        price = d0/rate

        print("Preferred Stock price: %f" % price)

    elif problemType == '19':
        rate = float(input("Rate of return: "))/100
        price = float(input("Price: "))

        dividend = price * rate

        print("Preferred Stock dividend: %f" % dividend)

    elif problemType == '20':
        price = float(input("Price: "))
        d0 = float(input("Annual Dividend: "))

        rate = d0/price * 100

        print("Preferred Stock rate of return: %f" % rate)

    elif problemType == '21':
        price = float(input("Price: "))
        d1 = float(input("D0: "))
        rate = float(input("Rate of Return: ")) / 100

        g = (rate - d1/price )* 100
        print("g = %f" % g)
    
    elif problemType == '22':
        numYears = int(input("Number of years until constant: "))
        yearsToDividend = int(input("Number of years until dividend paid: "))
        rate = float(input('Rate of return: ')) / 100
        D0 = float(input('D0: '))
        growthRates = []
        price = []

        for i in range(0,yearsToDividend):
            growthRates.append(0)
        
        for i in range(numYears-yearsToDividend):
            growthRates.append(float(input("growth rate in year %i: " % (i + 1 + yearsToDividend)))/100)
        
        dividends = [D0]

        for i in range(numYears-yearsToDividend):
            dividends.append(float(input("dividend rate in year %i: " % (i + yearsToDividend + 1))))

        lastPrice = dividends[-1] / (rate - growthRates[-1])
        print(lastPrice)

        currentPrice = 0
        for i in range(0, numYears - yearsToDividend):
            currentPrice += dividends[i]/pow(1+rate, yearsToDividend+i)
            if i == numYears - yearsToDividend - 1:
                currentPrice += lastPrice/pow(1+rate, yearsToDividend+i)
        print("current price: %f" % currentPrice)

    elif problemType == '23':
        p0 = float(input("P0: "))
        rate = float(input("Rate of Return: ")) / 100
        g = float(input("Growth Rate g: ")) / 100
        numYears = int(input("Number of years out: "))

        d1 = p0 * (rate - g)
        dividends = [d1]
        for i in range(1, numYears):
            dividends.append(dividends[i-1]*(1+g))
        print(dividends)
        finalPrice = dividends[-1] * (1 + g) / (rate - g)
        print(finalPrice)

    elif problemType == '24':
        d1 = float(input("D1: "))
        g = float(input("Growth Rate g: ")) / 100
        MRP = float(input("MRP: ")) / 100
        rRF = float(input("Risk Free Rate: ")) / 100
        beta = float(input("beta: "))

        rate = rRF + beta*(MRP)

        price = d1 / (rate - g)

        print("price: %f" % price)

    elif problemType == '25':
        rate = float(input("Rate of Return: ")) / 100
        numYears = int(input("Number of years: "))
        dividends = []
        for i in range(0, numYears):
            dividends.append(float(input("dividend rate in year %i: " % (i + 1))))

        currentPrice = 0
        for i in range(0, numYears):
            currentPrice += dividends[i]/pow(1+rate, i+1)
            
        print("current price: %f" % currentPrice)
        


    print("")

