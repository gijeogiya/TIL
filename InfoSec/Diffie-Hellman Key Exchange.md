# Diffie-Hellman Key Exchange
> Alice와 Bob이 하는 말을 Eve가(혹은 모두가) 들을 수 있는 상황에서 둘만 아는 Secret Key를 만드는 방법
- mod(코드에서 보통 `%`로 표시)
- 나머지 값을 구하는 Operator
- 예제
  - 7 mod 2 = 1
  - 9 mod 3 = 0
  - 12 mod 5 = 2
- 기억해야 될 mod의 특성
  - (g^a mod)^p = g^(ab) mod p
  - p 는 modulus
  - g 는 base
1. Alice는 p, g, a 값을 정한다. (단, p는 소수, g는 p의 primitive root modulo)
   - ex) p = 2, g = 5, a = 6
2. Alice는 Bob에게 p, g, g^a mod p 를 알려준다.
   - ex) Bod과 Eve는 p = 2, g = 5, g^a mod p = 8 을 알게된다.
3. Bob은 b 값을 정한다.
   - ex) b = 3
4. Bob은 Alice에게 g^b mod p 를 알려준다.
   - ex) Alice과 Eve는 g^b mod p = 10
5. Bob
