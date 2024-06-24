k, m, n = 15, 28, 24

#case 1 k + alpha
case1 = (k/(k+m+n)) * ((k-1)/(k-1+m+n)) \
+ (k/(k+m+n)) * (m/(k-1+m+n)) * 2 \
+ (k/(k+m+n)) * (n/(k-1+m+n)) * 2

#case 2 domi + rece
case2 = (m/(k+m+n)) * ((m-1)/(k+m+n-1)) * (3/4) \
+ (m/(k+m+n)) * (n/(k+m+n-1)) * 2 * (2/4)

#case 3 hetero + rece
case3 = (n/(k+m+n)) * ((n-1)/(k+m+n-1))

case1 + case2
