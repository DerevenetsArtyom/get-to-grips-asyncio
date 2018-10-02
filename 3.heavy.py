from main import lucas, async_print_matches, is_prime
from scheduler import Scheduler

scheduler = Scheduler()
scheduler.add(async_print_matches(lucas(), is_prime))
scheduler.run_to_completion()


