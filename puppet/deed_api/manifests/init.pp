# Install and configure the Flask Api Skeleton
class deed_api (
    $port = '9012',
    $host = '0.0.0.0',
    $branch_or_revision = 'master'
) {
  require ::standard_env

  vcsrepo { '/opt/deed_api':
    ensure   => latest,
    provider => git,
    source   => 'git://github.com/LandRegistry/charges-deed-api',
    revision => $branch_or_revision,
    owner    => 'vagrant',
    group    => 'vagrant',
    notify   => Service['deed_api'],
  }

  file { '/opt/deed_api/bin/run.sh':
    ensure  => 'file',
    mode    => '0755',
    owner   => 'vagrant',
    group   => 'vagrant',
    source  => "puppet:///modules/${module_name}/run.sh",
    require => Vcsrepo['/opt/deed_api'],
    notify  => Service['deed_api'],
  }

  file { '/etc/systemd/system/deed_api.service':
    ensure  => 'file',
    mode    => '0755',
    owner   => 'vagrant',
    group   => 'vagrant',
    content => template("${module_name}/service.systemd.erb"),
    notify  => [Exec['systemctl-daemon-reload'], Service['deed_api']],
  }
  service { 'deed_api':
    ensure   => 'running',
    enable   => true,
    provider => 'systemd',
    require  => [
      Vcsrepo['/opt/deed_api'],
      File['/opt/deed_api/bin/run.sh'],
      File['/etc/systemd/system/deed_api.service']
    ],
  }

  file { '/etc/nginx/conf.d/deed_api.conf':
    ensure  => 'file',
    mode    => '0755',
    content => template("${module_name}/nginx.conf.erb"),
    owner   => 'vagrant',
    group   => 'vagrant',
    notify  => Service['nginx'],
  }

}
