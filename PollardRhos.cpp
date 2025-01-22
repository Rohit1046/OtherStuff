#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int polynomial(long long x, long long n){
    return (x*x + 1) % n;
}

int main(){

    long long n;
    std :: cin >> n;

    long long xi = 2;

    std::vector<long long> sequence;
    sequence.push_back(xi);

    long long T=xi;
    long long H=xi;

    while(T!=H && T!=xi){
        T=polynomial(T,n);
        H=polynomial(polynomial(H,n),n);
        if(T==H){
            continue;
        }else{
            long long divisor = gcd(T-H,n);
            if(divisor==1){
                continue;
            }else{
                std::cout << "Divisors " << divisor << " " << n/divisor << "\n";
            }
        }

    }

    return 0;
}
