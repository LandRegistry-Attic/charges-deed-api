## Env.rb
#
# Env.rb is loaded in to every test. Thus any classes defined here
# can be used directly in any test.

# Env
#
# This class contains config values that can be used in tests
# In your steps just do:
#
#   Env.domain
class Env
  def self.domain
    (ENV['DOMAIN'] || 'http://localhost:5000')
  end
end
