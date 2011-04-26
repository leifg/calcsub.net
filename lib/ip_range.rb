require 'ipaddress'

class IpRange
  
  @Ip_helper
  @Net_address
  @Address
  
  def initialize(ip_address, prefix=nil)
    
    begin      
      unless prefix
        arr = ip_address.split('/')
        ip_address = arr[0]
        prefix = arr[1]
        
        unless prefix
    		tmp_ip_helper = IPAddress.parse(ip_address).max_prefix
        end
      end
      
      prefix = Integer(prefix)
      @Ip_helper = IPAddress.parse("#{ip_address}/#{prefix}")
    rescue
      @Ip_helper = BoringStub.new
    end
  end
  
  def separator
    @Ip_helper.separator
  end
  
  def valid?
    @Ip_helper.valid?
  end
  
  def split
    @Ip_helper.split
  end
  
  def to_s
    @Ip_helper.to_s
  end
  
  def size_of_sections
    @Ip_helper.size_of_sections
  end
  
  #important functions:
  
  def address
    @Ip_helper.address
  end
  
  def net_address
    @Ip_helper.network.address
  end
  
  def prefix
    @Ip_helper.prefix
  end
  
  def num_hosts
    
  end
  
  def num_nets
    
  end
  
  class BoringStub
    
    def network
      self
    end
    
    def prefix
      nil
    end
    
    def address
      nil
    end
    
    def valid?
      false
    end
    
    def split
      nil
    end
    
  end
  
end

class IPAddress::IPv6

  def size_of_sections
    4
  end

  def separator
    ':'
  end
  
  def max_prefix
  	128
  end

  def network
    self.class.parse_u128(network_u128, @prefix)
  end
  
  def valid?
    IPAddress::valid_ipv6? address
  end
  
  def sections
    hexs
  end
  
  def split
    Splitter.split(@prefix.to_i, sections, 16, 8)
  end
end

class IPAddress::IPv4
  
  def separator
    '.'
  end
  
  def size_of_sections
    3
  end
  
  def max_prefix
  	32
  end
  
  def valid?
    IPAddress::valid_ipv4? address
  end
  
  def split
    Splitter.split(@prefix.to_i, sections, 8, 4)
  end
  
  def sections
    string_octets = Array.new
    octets.each {|o| string_octets << "%03d" % o}
    string_octets
  end
  
end


# returns a data stucture that splits the ip address in 3 sections (net, host, mixed)
# example
# 
# "172.16.25.1/21".split:
# :net => ["172","016"]
# :host => ["001"]
# :mixed => ["025"] 
#
class Splitter
  
  def self.split(prefix, sections, bits_per_section, number_of_sections)
    net_sections = prefix / bits_per_section
    
    prefix_modulo = prefix % bits_per_section
    
    if (prefix_modulo == 0)
      mixed_sections = 0
    else
       mixed_sections = 1
    end
    
    host_sections = number_of_sections - net_sections - mixed_sections
    
    hash = Hash.new
    
    hash[:net] = sections[0,net_sections]
    hash[:mixed] = sections[net_sections,mixed_sections]
    hash[:host] = sections[net_sections+mixed_sections,host_sections]
    
    if (bits_per_section == 16 && prefix_modulo > 0)
      sub_hash = split(prefix_modulo, hash[:mixed][0].split(//), 4,4)
      
      hash[:net] << sub_hash[:net].join             unless sub_hash[:net].length == 0
      hash[:mixed] = sub_hash[:mixed]
      hash[:host].insert(0,sub_hash[:host].join)    unless sub_hash[:host].length == 0
    end
    
    hash
  end
end
