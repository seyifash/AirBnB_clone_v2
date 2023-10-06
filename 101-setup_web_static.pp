# Nginx configuration file

exec { 'system update':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['system update']
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
  ensure  => 'present',
  content => 'Holberton school',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true,
}

file { '/data/':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
$thecontent="location /hbnb_static/ {
	alias /data/web_static/current/;
	}"

file { '/etc/nginx/sites-enabled/default':
  ensure  => 'present',
  content => $thecontent
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
