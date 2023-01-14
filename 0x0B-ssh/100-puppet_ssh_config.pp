file { '/home/ubuntu/.ssh/config':
  ensure  => 'present',
  content => 'PasswordAuthentication no
IdentityFile ~/.ssh/school'
}
