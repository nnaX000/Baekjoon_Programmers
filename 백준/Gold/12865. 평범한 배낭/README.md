# [Gold V] 평범한 배낭 - 12865 

[문제 링크](https://www.acmicpc.net/problem/12865) 

### 성능 요약

메모리: 34972 KB, 시간: 3528 ms

### 분류

다이나믹 프로그래밍, 배낭 문제

### 제출 일자

2024년 3월 7일 16:10:52

### 문제 설명

<p>이 문제는 아주 평범한 배낭에 관한 문제이다.</p>

<p><span style="line-height:1.6em">한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.</span></p>

<p><span style="line-height:1.6em">준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.</span></p>

### 입력 

 <p>첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.</p>

<p>입력으로 주어지는 모든 수는 정수이다.</p>

### 출력 

 <p>한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.</p>

### 내가 놓쳤던 것

 <p>나는 그냥 이전 dp처럼 배열 잘 정렬해서 거기서 만들 수 있는 최댓값 찾으면서 차례차례 넘어가는 방식인 줄 알았는데 배열을 멜 수 있는 최대 무게만큼 만들어서 각 인덱스에 그 무게를 들때 최대가치를 저장하는 방식이 있었다..
 ex) array[4]=17 이면 가방 무게가 4일때 현재까지 나온 값 중 최대 가치는 17이라는 거
 그래서 입력받은 가방 무게랑 그 가치 하나씩 꺼내면서 이것보다 무거운 무게만 돌면서 
  
  1. 현재 그 index가 갖고 있는 최대 가치랑 
  2. 이제 막 꺼내온 가방 가치+(index-막 꺼내온 가방 무게)에 있는 최대가치 
 
 이렇게 두개 중 누가 더 큰지 해서 max값 갱신해주면 되는것이다.
 </p>


