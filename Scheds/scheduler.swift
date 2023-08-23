// Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import Foundation

/// Represents a job to be executed after a delay.
struct Job {
    let action: () -> Void
    let delay: Int
}
func executeJob(_ job: Job) {
    job.action()
}
import Dispatch

class JobScheduler {
    func schedule(job: Job) {
        DispatchQueue.global().asyncAfter(deadline: .now() + .milliseconds(job.delay)) {
            executeJob(job)
        }
    }
}
func testScheduler() {
    let scheduler = JobScheduler()

    let testCases: [Job] = [
        Job(action: { print("Job 1 executed!") }, delay: 1000),
        Job(action: { print("Job 2 executed!") }, delay: 2000),
        // ... Add more test cases as required
    ]

    for job in testCases {
        scheduler.schedule(job: job)
    }

    // Keep the main thread alive to allow async tasks to complete.
    RunLoop.current.run(until: Date().addingTimeInterval(10))
}

testScheduler()
