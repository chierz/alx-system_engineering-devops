# exec a command that kills a process 

exec {'pkill -f killmenow':
path => '/usr/bin/:/usr/local/bin/:/bin/',
}
