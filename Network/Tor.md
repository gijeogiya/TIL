# Tor(익명 네트워크)
## 특징
- Tor는 'The Onion Router'의 약칭이다. 네트워크 우회와 익명화를 위해 사용하는 툴 중 하나며, 딥 웹과 다크 웹에 이용되는 소프트웨어이다. 비슷한 것으론 Hyphanet(구 Freenet)과 I2P등이 있지만 토어는 세계적으로 가장 많이 쓰이고 있다. 많은 온라인 블랙마켓들이 .onion 도메인에 상주하고 있다.
- 프록시 서버나 서버에 로그가 남을 가능성이 있는 VPN보다 높은 수준의 익명성이 보장된다. 토어의 트래픽은 출발지에서 각각의 공개키로 순차적으로 암호화 된다. 3개 노드를 거친다면 3중 암호화해서 보내게 된다.
- 통신 속도가 느리다. 여러 국가의 네트워크를 경유하여 가기 때문이다. 예를 들면 자신의 컴퓨터 (한국) → 루마니아 (경유) → 러시아 연방 (경유) → 네덜란드 (경유) → 인터넷 식이다. 최종 인터넷 단계에서는 네덜란드에서 접속한 것으로 뜨게 된다. 정부가 만약 이를 역 추적하려 해도 네덜란드 → 러시아 연방 → 루마니아를 거쳐 실제 사용자의 컴퓨터까지 접근해야 하는 것이다.
## 동작 원리
- 토어는 목적지까지 한 번에 통신하지 않고, 중간에 같은 토어 라우터를 실행하고 있는 node들을 여러개 거쳐서 보낸다. 즉 A→Z 가 아니라 A→B→C→D→Z 로 빙빙 돌려서 보내는 식이다. 토어가 일반 브라우저에 비해 느린 이유가 바로 이 때문이다.
- 이름(양파 라우터)처럼 패킷을 양파 껍질처럼 겹겹이 암호화 해서 보내고, 이때 각각의 node의 공개키를 통해 암호화하므로, 패킷의 출발지와 목적지를 알아내려면 거의 모든 노드를 장악해야 한다. 예를 들면 위의 예시에서 정부기관(또는 해커)이 C 노드를 장악했다고 해도, "B에서 왔음, D로 보내시오"라는 정보밖에 알 수 없다.

![image](https://github.com/user-attachments/assets/d81777d0-7011-4bc9-bd3a-14ecfbed4822)
## 토어의 악용에 대한 토어 프로젝트의 입장
```
Q. 토어는 범죄자가 나쁜 일을 할 수 있게 하지 않습니까?
A. 범죄자들은 이미 나쁜 짓을 할 수 있습니다. 그들은 기꺼이 법을 위반하기 때문에 토어가 제공하는 것보다 더 나은 개인 정보 보호를 제공하는 많은 옵션을 이미 가지고 있습니다. 그들은 휴대폰을 훔쳐서 사용하고 도랑에 던질 수 있습니다. 그들은 한국이나 브라질의 컴퓨터에 침입하여 악의적인 활동을 시작하는 데 사용할 수 있습니다. 스파이웨어, 바이러스 및 기타 기술을 사용하여 문자 그대로 전 세계 수백만 대의 Windows 시스템을 제어할 수 있습니다.
토어는 법을 준수하고자 하는 일반 사람들을 보호하는 것을 목표로 합니다. 지금은 범죄자들만이 사생활을 가지고 있고 우리는 그것을 고쳐야 합니다.
익명성을 옹호하는 일부 사람들은 나쁜 용도를 좋은 용도로 받아들이는 것은 단지 절충안일 뿐이라고 설명하지만 그 이상의 의미가 있습니다. 범죄자 및 기타 나쁜 사람들은 좋은 익명성을 얻는 방법을 배우려는 동기가 있으며 많은 사람들이 이를 달성하기 위해 많은 비용을 지불하려는 동기를 가지고 있습니다. 무고한 피해자의 신원을 도용하고 재사용(신원 도용)할 수 있다는 점은 이를 더욱 쉽게 만듭니다. 반면에 일반 사람들은 온라인에서 개인 정보를 보호하는 방법을 알아내는 데 사용할 시간이나 돈이 없습니다. 이것은 모든 가능한 세계 중 최악입니다.
예, 범죄자는 토어를 사용할 수 있지만 이미 더 나은 옵션이 있으며 토어를 세상에서 제거한다고 해서 그들이 나쁜 일을 하는 것을 막을 수는 없을 것 같습니다. 동시에 토어 및 기타 개인 정보 보호 조치는 신원 도용, 스토킹과 같은 물리적 범죄 등과 싸울 수 있습니다.
```
```
Q. 토어 프로젝트는 기술을 사용하는 남용자에 대해 어디에 서 있습니까?
A. 우리는 남용을 심각하게 생각합니다. 활동가와 법 집행 기관은 토어를 사용하여 학대를 조사하고 생존자를 지원합니다. 우리는 그들과 협력하여 그들이 토어가 그들의 작업을 어떻게 도울 수 있는지 이해하도록 돕습니다. 경우에 따라 기술적 실수가 발생하고 있으며 이를 수정하는 데 도움을 줍니다. 생존자 커뮤니티의 일부 사람들은 연민 대신 낙인을 받아들이기 때문에 동료 피해자의 지원을 구하려면 개인 정보 보호 기술이 필요합니다.
우리가 토어에 백도어 구축과 검열을 거부하는 것은 우려가 부족해서가 아닙니다. 우리는 토어를 약화시키는 것을 거부합니다. 토어가 물리적 세계에서 아동 학대와 인신매매를 퇴치하려는 노력에 해를 끼치고 온라인에서 피해자를 위한 안전한 공간을 제거하기 때문입니다. 한편, 범죄자들은 여전히 봇넷, 도난당한 전화, 해킹된 호스팅 계정, 우편 시스템, 특사, 부패한 공무원 및 콘텐츠 거래를 위해 등장하는 모든 기술에 액세스할 수 있습니다. 그들은 기술의 얼리어답터입니다. 이에 직면하여 정책 입안자들이 차단 및 필터링으로 충분하다고 가정하는 것은 위험합니다. 우리는 정치인들이 그것을 숨겨서 유권자들에게 점수를 매기는 것을 돕는 것보다 아동 학대를 중단하고 예방하기 위한 노력을 돕는 데 더 관심이 있습니다. 부패의 역할은 특히 골칫거리입니다. 이 UN 보고서를 참조하십시오.인신매매에서 부패의 역할 .
마지막으로 아이들의 이름으로 정책을 추진할 때 아이들이 어른이 되어 마주하게 될 세상을 고려하는 것이 중요하다. 어른이 되어 안전하게 자신의 의견을 말할 수 없다면 우리에게 고마워할까요? 다른 아이들을 보호하기 위한 국가의 실패를 폭로하려는 경우에는 어떻게 해야 합니까?
```

![image](https://github.com/user-attachments/assets/58fbd053-59a6-45b5-95b5-1136e0ad5cc0)