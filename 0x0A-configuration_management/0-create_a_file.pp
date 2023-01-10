# create a file in /tmp

file { 'school':
  ensure  => 'present',
  owner   => 'www-data',
  path    => '/tmp/school',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
