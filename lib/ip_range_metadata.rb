require 'ipaddress'

class IpRangeMetadata
  
  @Ip_helper
  @Net_address
  @Address
  
  def initialize(ip_address, prefix=nil)
    
    begin
      if prefix
        @Ip_helper = IPAddress.parse("#{ip_address}/#{prefix}")
      else
        @Ip_helper = IPAddress.parse(ip_address)
      end
    rescue
      @Ip_helper = BoringStub.new
    end
    
    if prefix
      @Ip_helper = IPAddress.parse("#{ip_address}/#{prefix}") rescue BoringStub.new
    else
      @Ip_helper = IPAddress.parse(ip_address) rescue BoringStub.new
    end
  rescue  
    
  end
  
  def address
    @Ip_helper.address
  end
  
  def net_address
    @Ip_helper.network.address
  end
  
  def prefix
    @Ip_helper.prefix
  end
  
  def valid?
    @Ip_helper.valid?
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
    
  end
  
end

class IPAddress::IPv6

  def network
    self.class.parse_u128(network_u128, @prefix)
  end
  
  def valid?
    IPAddress::valid_ipv6? address
  end

end

class IPAddress::IPv4
  
  def valid?
    IPAddress::valid_ipv4? address
  end

end