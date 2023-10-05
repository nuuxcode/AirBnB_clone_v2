# instal and configure nginx
exec { 'update':
  command     => '/usr/bin/apt-get update',
  onlyif      => '/usr/bin/which nginx',
}
-> package { 'nginx':
  ensure => installed,
}
-> exec { 'run1':
  command => '/usr/bin/mkdir -p "/data/web_static/releases/test/" "/data/web_static/shared/"',
}
-> exec { 'run2':
  command => '/usr/bin/echo "Hi!" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
}
-> exec { 'run3':
  command => '/usr/bin/rm -rf /data/web_static/current',
}
-> exec { 'run4':
  command => '/usr/bin/ln -s /data/web_static/releases/test/ /data/web_static/current',
}
-> exec { 'run5':
  command => '/usr/bin/chown -R ubuntu:ubuntu /data/',
}
-> file_line { 'location_hbnb_static':
  path     => '/etc/nginx/sites-available/default',
  match    => '^server {',
  line     => 'server {\n\tlocation /hbnb_static {alias /data/web_static/current/;index index.html;}',
  multiple => false,
}
-> exec { 'run6':
  command => '/usr/sbin/service nginx restart',
}
