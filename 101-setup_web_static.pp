# instal and configure nginx
if ! which('nginx') {
  exec { 'update':
    command     => '/usr/bin/apt-get update',
  }
  -> package { 'nginx':
    ensure => installed,
  }
}
-> exec { 'run':
  command => '/usr/bin/mkdir -p "/data/web_static/releases/test/" "/data/web_static/shared/"',
}
-> exec { 'run':
  command => '/usr/bin/echo "Hi!" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
}
-> exec { 'run':
  command => '/usr/bin/rm -rf /data/web_static/current',
}
-> exec { 'run':
  command => '/usr/bin/ln -s /data/web_static/releases/test/ /data/web_static/current',
}
-> exec { 'run':
  command => '/usr/bin/chown -R ubuntu:ubuntu /data/',
}
-> file_line { 'location_hbnb_static':
  path     => '/etc/nginx/sites-available/default',
  match    => '^server {',
  line     => 'location /hbnb_static {alias /data/web_static/current/;index index.html;}',
  multiple => false,
}
-> exec { 'run':
  command => '/usr/sbin/service nginx restart',
}
