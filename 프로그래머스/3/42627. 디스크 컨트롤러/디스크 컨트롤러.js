function solution(jobs) {
    let ans = 0;
    let jobsCnt = jobs.length;
    if (jobsCnt === 0) return 0; // 작업이 없는 경우 0 반환

    jobs.sort((a, b) => a[0] - b[0] || a[1] - b[1]); // 요청 시점으로 먼저 정렬, 그 후 소요 시간으로 정렬

    let currentTime = jobs[0][0];
    let waitq = [];

    while (jobs.length > 0 || waitq.length > 0) {
        while (jobs.length > 0 && jobs[0][0] <= currentTime) {
            waitq.push(jobs.shift()); // 요청 시점이 현재 시간 이하인 작업을 대기열에 추가
        }

        if (waitq.length > 0) {
            waitq.sort((a, b) => a[1] - b[1]); // 대기열을 소요 시간이 짧은 순서로 정렬
            let waitingJob = waitq.shift();
            currentTime += waitingJob[1];
            ans += currentTime - waitingJob[0]; // 대기 시간 + 처리 시간
        } else {
            currentTime = jobs[0][0]; // 대기열이 비어있을 경우, 다음 작업의 요청 시점으로 현재 시간 갱신
        }
    }

    return Math.floor(ans / jobsCnt);
}
