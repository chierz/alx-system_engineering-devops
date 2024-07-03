# creates a file in /tmp

file{ 'file_name_is_just_me':
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
