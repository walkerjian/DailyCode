#include <iostream>
#include <functional>
#include <thread>

struct Job {
    std::function<void()> action;
    int delay;
};

void executeJob(const Job& job) {
    job.action();
}

class JobScheduler {
public:
    void schedule(const Job& job) {
        std::thread([job]() {
            std::this_thread::sleep_for(std::chrono::milliseconds(job.delay));
            executeJob(job);
        }).detach();
    }
};

void testScheduler() {
    JobScheduler scheduler;

    Job testCases[] = {
        { []() { std::cout << "Job 1 executed!" << std::endl; }, 1000 },
        { []() { std::cout << "Job 2 executed!" << std::endl; }, 2000 },
        // ... Add more test cases as required
    };

    for (const auto& job : testCases) {
        scheduler.schedule(job);
    }

    // Wait for a while to allow all jobs to complete.
    std::this_thread::sleep_for(std::chrono::seconds(10));
}

int main() {
    testScheduler();
    return 0;
}
