# sets up your web servers for the deployment of web_static
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure  => 'installed',
  require => Exec['update system;]
}

file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Holberton school',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true, 
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}

exec {'add':
  command => '/usr/bin/env  sed -i "/listen 80 default_server/a location /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n" '/etc/nginx/sites-enabled/default',
}

exec { 'service nginx restart':
  path => '/etc/init.d/'
}
