# Nginx configuration file

thecontent="location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }"

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure   => 'installed',
  provider => Exec['update system']
}

file { '/data':
  ensure  => 'directory'
}

file { '/data/web_static':
  ensure => 'directory'
}

file { '/data/web_static/releases':
  ensure => 'directory'
}

file { '/data/web_static/releases/test':
  ensure => 'directory'
}

file { '/data/web_static/shared':
  ensure => 'directory'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School Puppet\n"
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { 'configs':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'add_header X-Served-By \$hostname;',
  content => $thecontent,
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
