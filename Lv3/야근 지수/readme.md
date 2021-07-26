### 야근지수
---

n의 크기가 1,000,000 이므로 N^2은 불가능

따라서 Nlog(N) 또는 N 으로 해결해야 한다고 생각.

모든 제곱의 합이 가장 작으려면 극단적으로 크거나 작은 값이 존재하지 않는 방향으로 값들이 변화해야함.

따라서 매순간 최대값을 찾아야 하는데 일반적인 최댓값을 찾는 방식을 사용하게 될 경우 O(N)을 n번 반복해야 하므로 O(N^2)으로 

불가능.

따라서 **max-heap / min-heap**을 이용하여 O(logN) 복잡도로 max값 또는 min값을 push, pop 하고 이를 N번 반복하므로

O(NlogN) 으로 해결 가능.

> heap
> push, pop : O(logN)
> heapify : O(N)
> python의 경우 min heap이 default 이므로 -1을 곱해 음수로 넣게될 경우 max heap 활용가능.
