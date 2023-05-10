include stdlib

exec { 'fix-apache':
  command => 'sed -i "s/old_value/new_value/g" /etc/apache2/apache2.conf',
  onlyif  => 'grep old_value /etc/apache2/apache2.conf',
}

file_line { 'set-max-clients':
  ensure => present,
  path   => '/etc/apache2/apache2.conf',
  line   => 'MaxClients 150',
}

service { 'apache2':
  ensure    => running,
  subscribe => [ Exec['fix-apache'], File_line['set-max-clients'] ],
}

