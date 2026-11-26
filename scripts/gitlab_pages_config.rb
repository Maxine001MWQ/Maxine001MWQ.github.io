require 'uri'
require 'yaml'

url = URI.parse(ENV.fetch('CI_PAGES_URL'))
abort 'CI_PAGES_URL must be an absolute HTTP(S) URL' unless %w[http https].include?(url.scheme) && url.host
baseurl = url.path.sub(%r{/+$}, '')
url.path = ''
url.query = nil
url.fragment = nil
File.write(ARGV.fetch(0), { 'url' => url.to_s, 'baseurl' => baseurl }.to_yaml)
