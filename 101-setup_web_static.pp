# Nginx configuration file

exec { 'system update':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['system update']
}

file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  content => 'Holberton school',
}


file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true,
}

file { '/data'/:
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
$thecontent="location /hbnb_static/ {
	alias /data/web_static/current/;
	}"

file { '/etc/nginx/sites-available/hbnb_static':
  ensure  => 'file',
  content => $thecontent
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-enabled/hbnb_static'],
}
