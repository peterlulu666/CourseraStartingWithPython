def computepay(h, r):
    h = float(h)
    r = float(r)
    if h <= 40:
        pay = h * r
    else:
        pay = 40 * r + (h - 40) * r * 1.5
    return pay


hrs = float(input("Enter Hours:"))
rate_per_hour = float(input("Enter rate per hour:"))
p = computepay(hrs, rate_per_hour)
print("Pay", p)
